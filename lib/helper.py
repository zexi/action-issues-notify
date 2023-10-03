import time
from datetime import datetime, timedelta
from typing import List, Optional

from github import Github

def get_issues(repo, gh_token, since: Optional[int]=None, **kwargs):
    args = []
    if gh_token:
        args.append(gh_token)
    g = Github(*args)
    repo = g.get_repo(repo)
    kwargs['state'] = 'open'

    if since:
        now = datetime.now()
        recent_day = now - timedelta(days=since)
        kwargs['since'] = recent_day

    issues = repo.get_issues(**kwargs)
    t = time.time()
    issues = [i for i in issues if not i.pull_request]
    delta = int(time.time() - t)
    print(f'Fetch issues completed, total: {len(issues)}, elapsed: {delta}s')
    return issues


def get_recent_unhandled_issues(repo: str, gh_token: str, labels: List[str], since: int):
    issues = get_issues(repo, gh_token, since=since, labels=labels)
    return issues
#
#
# def send_recent_issue_alert_msg(args: argparse.ArgumentParser):
#     issues = get_recent_unhandled_issues()
#     kwargs = dict(recent=args.recent, repo=args.repo)


