class WorkOrder:
  def __init__(self, create_user="XXX", work_user="XXX", work_content="XXXXXXXXXX", start_time="2022-10-01", end_time="2022-10-01") -> None:
    # self.card_data = {
    #   "config" : {
    #     "update_multi" : True
    #   },
    #   "elements": [
    #     {
    #       "fields": [
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð£ï¸ åèµ·äººï¼**\n{create_user}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð¤ æ§è¡äººï¼**\n{work_user}",
    #             "tag": "lark_md"
    #           }
    #         }
    #       ],
    #       "tag": "div"
    #     },
    #     {
    #       "fields": [
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð å·¥ååå®¹ï¼**\n{work_content}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð ä»»å¡ç¶æï¼**\nå¾å¯å¨",
    #             "tag": "lark_md"
    #           }
    #         }
    #       ],
    #       "tag": "div"
    #     },
    #     {
    #       "fields": [
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð é¢è®¡å¼å§æ¶é´ï¼**\n{start_time}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**ð é¢è®¡ç»ææ¶é´ï¼**\n{end_time}",
    #             "tag": "lark_md"
    #           }
    #         }
    #       ],
    #       "tag": "div"
    #     },
    #     {
    #       "actions": [
    #         {
    #           "tag": "button",
    #           "text": {
    #             "content": "ç«å³å¤ç",
    #             "tag": "plain_text"
    #           },
    #           "type": "primary",
    #           "value": {
    #             "key1": "value1"
    #           }
    #         },
    #         {
    #           "tag": "button",
    #           "text": {
    #             "content": "å³é­å·¥å",
    #             "tag": "plain_text"
    #           },
    #           "type": "danger",
    #           "value": {
    #             "key2": "value2"
    #           }
    #         }
    #       ],
    #       "tag": "action"
    #     }
    #   ],
    #   "header": {
    #     "template": "blue",
    #     "title": {
    #       "content": "ðª ä½ æä¸æ¡æ°å·¥åéè¦å¤çï¼",
    #       "tag": "plain_text"
    #     }
    #   }
    # }

    self.card_data = {
      "config": {
        "update_multi": True
      },
      "elements": [
        {
          "fields": [
            {
              "is_short": True,
              "text": {
                "content": f"**ð£ï¸ åèµ·äººï¼**\n{create_user}",
                "tag": "lark_md"
              }
            },
            {
              "is_short": True,
              "text": {
                "content": f"**ð¤ æ§è¡äººï¼**\n{work_user}",
                "tag": "lark_md"
              }
            }
          ],
          "tag": "div"
        },
        {
          "fields": [
            {
              "is_short": False,
              "text": {
                "content": f"**ð å·¥ååå®¹ï¼**\n{work_content}",
                "tag": "lark_md"
              }
            }
          ],
          "tag": "div"
        },
        {
          "tag": "div",
          "text": {
            "tag": "lark_md",
            "content": "**ð ä»»å¡ç¶æï¼**"
          },
          "extra": {
            "tag": "select_static",
            "placeholder": {
              "tag": "plain_text",
              "content": "æªå¯å¨"
            },
            "value": {
              "key": "value"
            },
            "options": [
              {
                "text": {
                  "tag": "plain_text",
                  "content": ""
                },
                "value": "1"
              },
              {
                "text": {
                  "tag": "plain_text",
                  "content": "è¿è¡ä¸­"
                },
                "value": "2"
              },
              {
                "text": {
                  "tag": "plain_text",
                  "content": "å·²å®æ"
                },
                "value": "3"
              },
              {
                "text": {
                  "tag": "plain_text",
                  "content": "æªå®æ"
                },
                "value": "4"
              }
            ]
          }
        },
        {
          "tag": "div",
          "text": {
            "tag": "lark_md",
            "content": "**ð é¢è®¡å¼å§æ¶é´:** "
          },
          "extra": {
            "tag": "date_picker",
            "placeholder": {
              "tag": "plain_text",
              "content": "è¯·éæ©æ¥æ"
            },
            "initial_date": f"{start_time}"
          }
        },
        {
          "tag": "div",
          "text": {
            "tag": "lark_md",
            "content": "**ðï¸ é¢è®¡ç»ææ¶é´:** "
          },
          "extra": {
            "tag": "date_picker",
            "placeholder": {
              "tag": "plain_text",
              "content": "è¯·éæ©æ¥æ"
            },
            "initial_date": f"{end_time}"
          }
        },
        {
          "actions": [
            {
              "tag": "button",
              "text": {
                "content": "æ¥æ¶å·¥å",
                "tag": "plain_text"
              },
              "type": "primary",
              "value": {
                "key1": "value1"
              }
            },
            {
              "tag": "button",
              "text": {
                "content": "å³é­å·¥å",
                "tag": "plain_text"
              },
              "value": {
                "key2": "value2"
              }
            }
          ],
          "tag": "action"
        }
      ],
      "header": {
        "template": "blue",
        "title": {
          "content": "ðª ä½ æä¸æ¡æ°å·¥åéè¦å¤çï¼",
          "tag": "plain_text"
        }
      }
    }