import requests
from issue import get_issue
from code_diffs import get_changed_files, get_code_diffs
import configparser

config = configparser.ConfigParser()
config.read("../config.ini")

github_token = config["github"]["token"]
github_api_version = config["github"]["api_version"]


def get_pull_request_data(owner: str, repo: str, pull_request_number: int) -> dict:
    pull_request_url = (
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}"
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": github_api_version,
    }
    return requests.get(pull_request_url, headers=headers).json()


def get_title(pull_request_data: dict) -> str:
    if "title" in pull_request_data.keys():
        return pull_request_data["title"]
    return ""


def get_description(pull_request_data: dict) -> str:
    if "description" in pull_request_data.keys():
        return pull_request_data["description"]
    return ""


def get_data_from_pr(owner: str, repo: str, pull_request_number: int) -> dict:
    data = get_pull_request_data(owner, repo, pull_request_number)
    title = get_title(data)
    description = get_description(data)
    issue = get_issue(data)
    changed_files = get_changed_files(owner, repo, pull_request_number)
    code_diff = get_code_diffs(data)
    return {
        "title": title,
        "description": description,
        "issue": issue,
        "changed_files": changed_files,
        "code_diffs": code_diff,
    }