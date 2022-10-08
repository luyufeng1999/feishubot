import json
from api import MessageApiClient
from event import MessageReceiveEvent
from utils import dict_2_obj

class handle:
    def __init__(message):
        return  
def encapsulate_text(text : str):
    data = {
        "text" : text
    }
    return json.dumps(data)

def return_send_type(msg : str):
    return {
        "type" : "send",
        "data" : msg
    }

def text_msg_handle(req_data : MessageReceiveEvent, message_api_client : MessageApiClient):
    sender_id = req_data.event.sender.sender_id
    message = req_data.message;
    content = message.content
    dict_data = json.loads(content)
    text_obj = dict_2_obj(dict_data)



msg_type_dict = {}
msg_type_dict['text'] = text_msg_handle

def handler_msg(req_data : MessageReceiveEvent, message_api_client : MessageApiClient):
    sender_id = req_data.event.sender.sender_id
    message = req_data.message;
    msg_type_dict[message.message_type](req_data, message_api_client)
        
    
