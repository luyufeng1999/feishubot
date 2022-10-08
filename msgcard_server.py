#!/usr/bin/env python3.8

import os
import logging
import requests
from api import MessageApiClient, UserApiClient
from card import WorkOrder
from event import MessageReceiveEvent, UrlVerificationEvent, EventManager
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv
import json
import msg_handler

import re

# load env parameters form file named .env
load_dotenv(find_dotenv())

app = Flask(__name__)

# load from env
APP_ID = "cli_a3b9601adcbad00e"
APP_SECRET = "w6VaZF9hB8Tj5jaukV1TlFfWRsiZ2blX"
VERIFICATION_TOKEN = "s5qwks75IGBFmAq01ve0ngKQqBhJFQF4"
ENCRYPT_KEY = "EGKrx2ddCKnPxbCoPPoUNeF7pc3ELeeV"
LARK_HOST = os.getenv("LARK_HOST")
print(LARK_HOST);

event_manager = EventManager()


# url验证事件(飞书验证url时调用)
@event_manager.register("url_verification")
def request_url_verify_handler(req_data: UrlVerificationEvent):
    # url verification, just need return challenge
    if req_data.event.token != VERIFICATION_TOKEN:
        raise Exception("VERIFICATION_TOKEN is invalid")
    return jsonify({"challenge": req_data.event.challenge})

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
