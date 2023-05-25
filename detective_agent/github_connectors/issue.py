def get_issue(pull_request_data: dict) -> str:
    if "issue_url" in pull_request_data.keys():
        return pull_request_data["issue_url"].split("issues/")[1]
    return ""
