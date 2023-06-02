import os
import csv


def write_to_csv(headers: list, data: list, filename: str):
    f = open(filename, "a")
    file_exists = os.path.isfile(filename) and os.stat(filename).st_size != 0
    writer = csv.DictWriter(f, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerows(data)
    f.close()


def find_max_index(lst):
    if len(lst) == 0:
        return None  # Return None if the list is empty
    max_index = lst.index(max(lst))
    return max_index
