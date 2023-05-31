import random


def select_unique_pairs(lst: list, number_pairs: int, max_iterations: int) -> list:
    pairs = set()
    iterations = 0

    while len(pairs) < number_pairs and iterations < max_iterations:
        pair = random.sample(lst, 2)
        if pair[0] != pair[1] and pair not in list(pairs):
            pairs.add(tuple(pair))

        iterations += 1
    return list(pairs)


def write_to_md(repo: str, pull_requests_list: list):
    f = open("scraped_data.md", "a")
    for pull_requests in pull_requests_list:
        pull_request_nos = [pull_requests[0].split("pulls/")[1]], pull_requests[
            1
        ].split("pulls/")[1]
        append_data = "| {} | [{}]({}), [{}]({}) |\n".format(
            repo,
            pull_request_nos[0],
            pull_requests[0],
            pull_request_nos[1],
            pull_requests[1],
        )
        f.write(append_data)
    f.close()
