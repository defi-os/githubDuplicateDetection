from detective_agent.config import md_path, reformatted_md_write_path
from detective_agent.model.Dataset.scrap_data.utils import write_to_csv
import re


def read_markdown_data(filename):
    with open(filename, "r") as file:
        markdown_data = file.read()
    return markdown_data


def parse_markdown_and_push_csv(markdown_data):
    # Extract rows from Markdown data using regular expressions
    rows = re.findall(r"\| ([^\|]+) \| \[([^]]+)\]", markdown_data)
    for row in rows:
        repo = row[0].strip()
        pull_requests = row[1].split(", ")
        pr1 = pull_requests[0]
        pr2 = pull_requests[1] if len(pull_requests) > 1 else ""
        unique_pull_requests_pair = (pr1, pr2)
        write_to_csv(repo, unique_pull_requests_pair, "True", reformatted_md_write_path)
