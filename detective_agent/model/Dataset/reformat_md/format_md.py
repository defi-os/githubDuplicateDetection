from detective_agent.config import md_path, reformatted_csv_write_path
from detective_agent.model.Dataset.scrap_data.utils import write_to_csv


def read_markdown_data(filename):
    with open(filename, "r") as file:
        markdown_data = file.read()
    return markdown_data


def parse_markdown_and_push_csv(markdown_data):
    # Extract rows from Markdown data using regular expressions
    for row in markdown_data.split("\n"):
        row = row.split("|", maxsplit=2)
        repo = row[1].strip()
        pr1 = row[2].split("(", maxsplit=1)[1].split(")", maxsplit=1)[0].strip()
        pr2 = row[2].rsplit("(", maxsplit=1)[1].split(")", maxsplit=1)[0].strip()
        unique_pull_requests_pair = [(pr1, pr2)]
        write_to_csv(
            repo, unique_pull_requests_pair, "True", reformatted_csv_write_path
        )


parse_markdown_and_push_csv(read_markdown_data(md_path))
