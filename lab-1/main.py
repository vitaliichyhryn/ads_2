import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr):
    num_of_ops = 0
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - i - 1):
            num_of_ops += 1
            if arr[j] > arr[j + 1]:
                num_of_ops += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return num_of_ops


def modified_bubble_sort(arr):
    num_of_ops = 0
    arr_len = len(arr)
    for i in range(arr_len):
        swapped = False
        for j in range(arr_len - i - 1):
            num_of_ops += 1
            if arr[j] > arr[j + 1]:
                num_of_ops += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return num_of_ops


gaps = [1750, 701, 301, 132, 57, 23, 10, 4, 1]


def shell_sort(arr):
    num_of_ops = 0
    arr_len = len(arr)
    for gap in gaps:
        for i in range(gap, arr_len):
            num_of_ops += 1
            temp = arr[i]
            j = i
            while j >= gap:
                num_of_ops += 1
                if arr[j - gap] > temp:
                    num_of_ops += 1
                    arr[j] = arr[j - gap]
                    j -= gap
                else:
                    break
            num_of_ops += 1
            arr[j] = temp
    return num_of_ops


sizes = [10, 100, 1000, 5000, 10000, 20000, 50000]

nums_of_ops = []
for size in sizes:
    arr = np.arange(size)  # sorted array
    print(f"Sorted array: {arr}")
    num_of_ops = shell_sort(arr)
    nums_of_ops.append(num_of_ops)
    print(f"Sorted array: {arr}\n"
          f"Number of operations: {nums_of_ops}")
plt.plot(sizes, nums_of_ops, 'g.-', label="Sorted array")

input("\ndone, press any key to continue\n")

nums_of_ops = []
for size in sizes:
    arr = np.arange(size - 1, -1, -1)  # reverse sorted array
    print(f"Reverse sorted array: {arr}")
    num_of_ops = shell_sort(arr)
    nums_of_ops.append(num_of_ops)
    print(f"Sorted array: {arr}\n"
          f"Number of operations: {nums_of_ops}")
plt.plot(sizes, nums_of_ops, 'r.-', label="Reverse sorted array")

input("\ndone, press any key to continue\n")

nums_of_ops = []
for size in sizes:
    arr = [np.random.randint(0, 1024) for i in range(size)]  # random array
    print(f"Random array: {arr}")
    num_of_ops = shell_sort(arr)
    nums_of_ops.append(num_of_ops)
    print(f"Sorted array: {arr}\n"
          f"Number of operations: {nums_of_ops}")
plt.plot(sizes, nums_of_ops, 'b.-', label="Random array")

input("\ndone, press any key to continue\n")

xs = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])

# ys = xs**2
# plt.plot(xs, ys, 'm.--', label="n^2")  # bubble

# ys = xs
# plt.plot(xs, ys, 'y.--', label="n")  # mod bubble

ys = xs*((np.log2(xs)**2)/(np.log2(np.log2(xs))))
plt.plot(xs, ys, 'm.--', label="n*log^2(n)/log(log(n))")  # shell

ys = xs*np.log2(xs)
plt.plot(xs, ys, 'y.--', label="n*log(n)")  # shell

plt.title("Shell sort")

plt.xlabel("Array size")
plt.ylabel("Number of operations")

plt.xscale("log")

plt.legend()
plt.show()
