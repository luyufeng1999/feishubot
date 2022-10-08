#!/usr/bin/env python3.8

import os
import logging
import requests
from api import MessageApiClient, UserApiClient
from card import WorkOrder
from event import MessageCardCallbackEvent, MessageReceiveEvent, UrlVerificationEvent, EventManager
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv
import json
import msg_handler

import re

# load env parameters form file named .env
load_dotenv(find_dotenv())

app = Flask(__name__)

# load from env
APP_ID = os.getenv("APP_ID")
APP_SECRET = os.getenv("APP_SECRET")
VERIFICATION_TOKEN = os.getenv("VERIFICATION_TOKEN")
ENCRYPT_KEY = os.getenv("ENCRYPT_KEY")
LARK_HOST = os.getenv("LARK_HOST")
print(LARK_HOST);

# init service
message_api_client = MessageApiClient(APP_ID, APP_SECRET, LARK_HOST)
user_api_client = UserApiClient(APP_ID, APP_SECRET, LARK_HOST)
event_manager = EventManager()


# url验证事件(飞书验证url时调用)
@event_manager.register("url_verification")
def request_url_verify_handler(req_data: UrlVerificationEvent):
    # url verification, just need return challenge
    if req_data.event.token != VERIFICATION_TOKEN:
        raise Exception("VERIFICATION_TOKEN is invalid")
    return jsonify({"challenge": req_data.event.challenge})

# 机器人接收消息事件
@event_manager.register("im.message.receive_v1")
def message_receive_event_handler(req_data: MessageReceiveEvent):
    sender_id = req_data.event.sender.sender_id
    message = req_data.event.message
    if message.message_type != "text":
        logging.warn("Other types of messages have not been processed yet")
        return jsonify()

    
    content = json.loads(message.content)
    p = re.compile("@(.*) 给@(.*) 派单,工作内容:(.*),预计开始时间:(.*),预计完成时间:(.*)")
    m = p.search(content['text'])
    if m != None:
        create_user = user_api_client.get_user_info_with_user_id(sender_id.user_id).get("name")
        user = message.mentions[1].name
        work_content = m.group(3)
        start_time = m.group(4)
        end_time = m.group(5)
        work_order = WorkOrder(create_user, user, work_content, start_time, end_time)
        if message.chat_type == "group":
            message_api_client.send_card("chat_id", message.chat_id, work_order.card_data)
        else:
            message_api_client.send_card("open_id", message.mentions[1].id.open_id, work_order.card_data)
    elif "需求单" in content['text']:
        work_order = WorkOrder()
        message_api_client.send_card("chat_id", message.chat_id, work_order.card_data)
        
    # msg_handler.handler_msg(req_data, message_api_client)
    return jsonify()

@event_manager.register("message_card.callback")
def message_receive_event_handler(req_data: MessageCardCallbackEvent):
    
    return jsonify()


@app.errorhandler
def msg_error_handler(ex):
    logging.error(ex)
    response = jsonify(message=str(ex))
    response.status_code = (
        ex.response.status_code if isinstance(ex, requests.HTTPError) else 500
    )
    return response


@app.route("/", methods=["POST"])
def callback_event_handler():
    # init callback instance and handle
    print("Post请求到了这")
    event_handler, event = event_manager.get_handler_with_event(VERIFICATION_TOKEN, ENCRYPT_KEY)

    return event_handler(event)


if __name__ == "__main__":
    # init()
    app.run(host="0.0.0.0", port=3000, debug=True)
