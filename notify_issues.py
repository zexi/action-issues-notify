#!/usr/bin/python3

import os
import json

import requests


class Input:

    def __init__(self):
        print(os.environ)
        self.url = os.environ.get('INPUT_URL')
        self.issue_title = os.environ.get('INPUT_ISSUE_TITLE')
        self.issue_body = os.environ.get('INPUT_ISSUE_BODY')
        self.issue_link_url = os.environ.get('INPUT_ISSUE_LINK_URL')

    def __repr__(self) -> str:
        return str({
            'url': self.url,
            'issue_title': self.issue_title,
            'issue_body': self.issue_body,
            'issue_link_url': self.issue_link_url
        })

    def send_post(self):
        headers = {"Content-Type":"application/json"}
        body = {
            "msg_type": "post",
            "content": {
                "post": {
                    "zh_cn": {
                        "title": self.issue_title,
                        "content": [
                            [
                                {
                                "tag": "text",
                                "text": json.loads(self.issue_body)
                                }
                            ],
                            [
                                {
                                    "tag": "text",
                                    "text": "\n",
                                },
                                {
                                "tag": "a",
                                "text": "查看原文",
                                "href": self.issue_link_url,
                                }
                            ]
                        ]
                    }
                }
            }
        }
        print(f'=== send body: {body}')
        res = requests.post(url=self.url, data=json.dumps(body), headers=headers)
        print(f'=== response: {res.text}')
        print(f'send status code: {res.status_code}')

    def send(self):
        headers = {"Content-Type":"application/json"}
        body = json.dumps(
            {
                "msg_type": "interactive",
                "card": {
                    "header": {
                        "template": "blue",
                        "title": {
                            "tag": "plain_text",
                            "content": self.issue_title,
                        }
                    },
                    "elements": [
                        # {
                        #     "tag": "div",
                        #     "text": {
                        #         "content": json.loads(self.issue_body),
                        #         "tag": "lark_md"
                        #     }
                        # },
                        {
                            "tag": "markdown",
                            "content": json.loads(self.issue_body),
                        },
                        {
                            "tag": "div",
                            "text": {
                                "content": f"[查看原文]({self.issue_link_url})",
                                "tag": "lark_md"
                            }
                        }
                        # {
                        #     "tag": "action",
                        #     "actions": [
                        #         {
                        #             "tags": "button",
                        #             "text": {
                        #                 "content": "查看链接",
                        #                 "tag": "plain_text"
                        #             },
                        #             "type": "primary",
                        #             "url": self.issue_link_url
                        #         },
                        #     ],
                        # },
                    ],
                },
            })
        print(f'=== send body: {body}')
        res = requests.post(url=self.url, data=body, headers=headers)
        print(f'=== response: {res.text}')
        print(f'send status code: {res.status_code}')


def main():
    input_vars = Input()
    input_vars.send_post()


if __name__ == '__main__':
    main()
