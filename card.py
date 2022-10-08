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
    #             "content": f"**🗣️ 发起人：**\n{create_user}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**👤 执行人：**\n{work_user}",
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
    #             "content": f"**📚 工单内容：**\n{work_content}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**📌 任务状态：**\n待启动",
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
    #             "content": f"**📅 预计开始时间：**\n{start_time}",
    #             "tag": "lark_md"
    #           }
    #         },
    #         {
    #           "is_short": True,
    #           "text": {
    #             "content": f"**📆 预计结束时间：**\n{end_time}",
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
    #             "content": "立即处理",
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
    #             "content": "关闭工单",
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
    #       "content": "📪 你有一条新工单需要处理！",
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
                "content": f"**🗣️ 发起人：**\n{create_user}",
                "tag": "lark_md"
              }
            },
            {
              "is_short": True,
              "text": {
                "content": f"**👤 执行人：**\n{work_user}",
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
                "content": f"**📚 工单内容：**\n{work_content}",
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
            "content": "**📌 任务状态：**"
          },
          "extra": {
            "tag": "select_static",
            "placeholder": {
              "tag": "plain_text",
              "content": "未启动"
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
                  "content": "进行中"
                },
                "value": "2"
              },
              {
                "text": {
                  "tag": "plain_text",
                  "content": "已完成"
                },
                "value": "3"
              },
              {
                "text": {
                  "tag": "plain_text",
                  "content": "未完成"
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
            "content": "**📅 预计开始时间:** "
          },
          "extra": {
            "tag": "date_picker",
            "placeholder": {
              "tag": "plain_text",
              "content": "请选择日期"
            },
            "initial_date": f"{start_time}"
          }
        },
        {
          "tag": "div",
          "text": {
            "tag": "lark_md",
            "content": "**🗓️ 预计结束时间:** "
          },
          "extra": {
            "tag": "date_picker",
            "placeholder": {
              "tag": "plain_text",
              "content": "请选择日期"
            },
            "initial_date": f"{end_time}"
          }
        },
        {
          "actions": [
            {
              "tag": "button",
              "text": {
                "content": "接收工单",
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
                "content": "关闭工单",
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
          "content": "📪 你有一条新工单需要处理！",
          "tag": "plain_text"
        }
      }
    }