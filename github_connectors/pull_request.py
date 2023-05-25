import requests
from issue import get_issue
from code_diffs import get_code_diffs

def get_pull_request_data(owner: str, repo: str, pull_request_number:int) -> dict:
    pull_request_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}"
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer <YOUR-TOKEN>',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    return requests.get(pull_request_url,headers=headers).json()

def get_title(pull_request_data:dict) -> str:
    if "title" in pull_request_data.keys():
        return pull_request_data["title"]
    return ""

def get_description(pull_request_data:dict)->str:
    if "description" in pull_request_data.keys():
        return pull_request_data["description"]
    return ""

def get_data_from_pr(owner: str, repo: str, pull_request_number: int) -> dict:
    data = get_pull_request_data(owner,repo,pull_request_number)
    title = get_title(data)
    description = get_description(data)
    issue = get_issue(data)
    code_diffs = get_code_diffs(pull_request_number)
    return {
        "title":title,
        "description": description,
        "issue": issue,
        "code_diffs": code_diffs
    }