import sys


def knapsack(weights, values, capacity, item_num, stored):
    if item_num == 0 or capacity == 0:
        return 0
    if stored[item_num][capacity] != -1:
        return stored[item_num][capacity]

    if weights[item_num - 1] <= capacity:
        stored[item_num][capacity] = max(
            values[item_num - 1] + knapsack(weights, values, capacity - weights[item_num - 1], item_num - 1, stored),
            knapsack(weights, values, capacity, item_num - 1, stored))
        return stored[item_num][capacity]
    elif weights[item_num - 1] > capacity:
        stored[item_num][capacity] = knapsack(weights, values, capacity, item_num - 1, stored)
        return stored[item_num][capacity]


def read_arr(path):
    with open(path) as file:
        lines = file.readlines()
        return [list(map(int, line.split())) for line in lines]


if __name__ == '__main__':
    args = sys.argv[1:]
    table = read_arr(args[0])
    capacity = table[0][0]
    item_num = table[0][1]
    items = table[1:]
    stored = [[-1 for _ in range(capacity + 1)] for _ in range(item_num + 1)]
    with open("output.txt", 'w') as file:
        value = knapsack([item[1] for item in items], [item[0] for item in items], capacity, item_num, stored)
        file.write(str(value))
