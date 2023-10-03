#!/usr/bin/python3

import os

from github import Label, Issue

from lib import helper

awaiting_processing = 'state/awaiting processing'
awaiting_user_feedback = 'state/awaiting user feedback'

def is_issue_contains_labels(i: Issue.Issue, il: list[str]):
    labels = i.labels
    cur_labels = [l.name for l in labels]
    for check_l in il:
        if check_l in cur_labels:
            return True
    return False


def add_issue_labels(i: Issue.Issue):
    # import ipdb; ipdb.set_trace()
    i.add_to_labels(awaiting_processing)


if __name__ == '__main__':
    labels = [awaiting_processing, awaiting_user_feedback, 'announcement']
    gh_token = os.environ.get('GITHUB_TOKEN', '')
    issues = helper.get_issues('yunionio/cloudpods', gh_token, 30, labels=[])

    foud_issues = []
    for i in issues:
        if not is_issue_contains_labels(i, labels):
            foud_issues.append(i)
    print(foud_issues)
    for i in foud_issues:
        add_issue_labels(i)

