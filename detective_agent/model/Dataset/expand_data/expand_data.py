from detective_agent.config import reformatted_csv_write_path
from detective_agent.github_connectors.pull_request import get_data_from_pr
from detective_agent.model.Dataset.expand_data.utils import write_to_csv
import csv


def reformat_data(filename):
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = []
        i = 0
        for row in csv_reader:
            split_repo = row["Repo"].split("/")
            pr_data_1 = get_data_from_pr(
                split_repo[0], split_repo[1], row["PullRequest1"]
            )
            pr_data_2 = get_data_from_pr(
                split_repo[0], split_repo[1], row["PullRequest2"]
            )
            changed_files_1 = set(
                [
                    changed_files["filename"]
                    for changed_files in pr_data_1["changed_files"]
                ]
            )
            changed_files_2 = set(
                [
                    changed_files["filename"]
                    for changed_files in pr_data_2["changed_files"]
                ]
            )
            data.append(
                {
                    "Repo": split_repo[0],
                    "owner": split_repo[1],
                    "PullRequest1": row["PullRequest1"],
                    "PullRequest2": row["PullRequest2"],
                    "PR1Title": pr_data_1["title"],
                    "PR2Title": pr_data_2["title"],
                    "PR1Desc": pr_data_1["description"],
                    "PR2Desc": pr_data_2["description"],
                    "PR1codediff": pr_data_1["code_diffs"],
                    "PR2codediff": pr_data_2["code_diffs"],
                    "changed_files": changed_files_1.symmetric_difference(
                        changed_files_2
                    ),
                }
            )
            print(i)
            i += 1
        headers = list(data[0].keys())
        write_to_csv(headers, data, "all_data.csv")


reformat_data(reformatted_csv_write_path)
