import requests

def get_code_diffs_data(owner: str, repo: str, pull_request_number:int) -> dict:
    code_diffs_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}/files"
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer <YOUR-TOKEN>',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    return requests.get(code_diffs_url,headers=headers).json()

def get_code_diffs(repo:str,owner:str,pull_request_number:int) -> list:
    code_diffs_data = get_code_diffs_data(repo,owner,pull_request_number)
    files = []
    for data in code_diffs_data:
        files.append({
            "filename":data["filename"],
            "additions":data["additions"],
            "deletions":data["deletions"],
            "changes":data["changes"]
        })
    return files