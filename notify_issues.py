#!/usr/bin/python3

import textwrap
import datetime
import argparse
import os

import requests

from lib.helper import get_recent_unhandled_issues


parser = argparse.ArgumentParser(description='Check issue states and do notification')
parser.add_argument('repo', type=str, help='Github repository, e.g. yunionio/cloudpods')
parser.add_argument('--hook', type=str, help='Notification webhook URL')

args = parser.parse_args()


def main():
    # send_recent_issue_alert_msg()
    pass


if __name__ == '__main__':
    # main()
    labels = ['state/awaiting processing']
    gh_token = os.environ.get('GITHUB_TOKEN', '')
    issues = get_recent_unhandled_issues('yunionio/cloudpods', gh_token, labels, 30)
    for i in issues:
        print(i)
