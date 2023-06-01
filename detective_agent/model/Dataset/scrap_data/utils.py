import random
import csv
import os


def select_unique_pairs(lst: list, number_pairs: int, max_iterations: int) -> list:
    pairs = set()
    iterations = 0

    while len(pairs) < number_pairs and iterations < max_iterations:
        pair = random.sample(lst, 2)
        if pair[0] != pair[1] and pair not in list(pairs):
            pairs.add(tuple(pair))

        iterations += 1
    return list(pairs)


def write_to_csv(repo: str, pull_requests_list: list):
    filename = "scraped_data.csv"
    f = open(filename, "a")
    file_exists = os.path.isfile(filename) and os.stat(filename).st_size != 0
    headers = ["Repo", "PullRequest1", "PullRequest2", "copied"]
    writer = csv.DictWriter(f, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    data = []
    for pull_requests in pull_requests_list:
        data.append(
            {
                "Repo": repo,
                "PullRequest1": pull_requests[0].split("pulls/")[1],
                "PullRequest2": pull_requests[1].split("pulls/")[1],
                "copied": "False",
            }
        )
    writer.writerows(data)
    f.close()
