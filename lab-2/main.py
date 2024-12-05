import sys
from pathlib import Path


def merge_count_invs(left_list, right_list):
    left_list_len, right_list_len = len(left_list), len(right_list)
    sorted_list = []
    invs = 0
    i = j = 0
    while i < left_list_len and j < right_list_len:
        if left_list[i] < right_list[j]:
            sorted_list.append(left_list[i])
            i += 1
        else:
            sorted_list.append(right_list[j])
            j += 1
            invs += left_list_len - i
    return sorted_list + left_list[i:] + right_list[j:], invs


def count_invs(rel_list):
    list_len = len(rel_list)
    mid = list_len // 2
    if list_len == 1:
        return rel_list, 0
    left_list, right_list = rel_list[:mid], rel_list[mid:]
    left_list, left_invs = count_invs(left_list)
    right_list, right_invs = count_invs(right_list)
    rel_list, cross_invs = merge_count_invs(left_list, right_list)
    return rel_list, left_invs + right_invs + cross_invs

def get_rel_list(rating_list, rating_list_compare):
    list_len = len(rating_list)
    rel_list = [0 for _ in range(list_len)]
    for i in range(list_len):
        rel_list[rating_list_compare[i] - 1] = rating_list[i]
    return rel_list


def read_table(filename):
    with Path(filename).open() as file:
        lines = file.readlines()
    return [list(map(int, line.split())) for line in lines]


if __name__ == "__main__":
    args = sys.argv[1:]
    table = read_table(args[0])
    user = int(args[1])
    output = [[row[0], count_invs(get_rel_list(table[user][1:], row[1:]))[1]] for row in table[1:] if row[0] != user]
    output.sort(key=lambda invs: invs[1])
    output_str = "\n".join(" ".join(map(str, row)) for row in output)
    with Path("output.txt").open("w") as file:
        file.write(f"{user}\n{output_str}\n")
