from re import S


import json

class ResultType:
    def __init__(self):
        self.type = "default"


class Send(ResultType):
    def __init__(self):
        self.type = "send"
        self.send_type = "text"
        self.data = "default text"
        
class SendText(Send):
    def __init__(self, text : str):
        self.data = json.dumps({
            "text" : text
        })
