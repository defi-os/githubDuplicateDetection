import requests
from detective_agent.config import github_token, github_api_version


def get_code_diffs_data(owner: str, repo: str, pull_request_number: int) -> dict:
    code_diffs_url = (
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}/files"
    )
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {github_token}",
        "X-GitHub-Api-Version": github_api_version,
    }
    return requests.get(code_diffs_url, headers=headers).json()


def get_changed_files(repo: str, owner: str, pull_request_number: int) -> list:
    code_diffs_data = get_code_diffs_data(repo, owner, pull_request_number)
    files = []
    for data in code_diffs_data:
        files.append(
            {
                "filename": data["filename"],
                "additions": data["additions"],
                "deletions": data["deletions"],
                "changes": data["changes"],
            }
        )
    return files


def get_code_diffs(pull_request_data: dict) -> str:
    if "diff_url" in pull_request_data.keys():
        code_diff = requests.get(pull_request_data["diff_url"]).content
        try:
            return code_diff.decode("ascii")
        except:
            return code_diff.decode("utf-8", errors="replace")
    return ""
