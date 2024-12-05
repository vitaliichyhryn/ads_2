import sys
import numpy as np
import matplotlib.pyplot as plt


def last_qsort(arr, lo, hi):
    if lo < hi:
        p = last_part(arr, lo, hi)
        last_qsort(arr, lo, p - 1)
        last_qsort(arr, p + 1, hi)
    return arr


def last_part(arr, lo, hi):
    global comps
    p = arr[hi]
    i = lo
    for j in range(lo, hi):
        comps += 1
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def ins_sort(arr, lo, hi):
    global comps
    for i in range(lo + 1, hi + 1):
        key = arr[i]
        j = i - 1
        while j >= lo:
            comps += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = key


def med_qsort(arr, lo, hi):
    if hi - lo <= 3:
        ins_sort(arr, lo, hi)
    elif lo < hi:
        p = med_part(arr, lo, hi)
        med_qsort(arr, lo, p - 1)
        med_qsort(arr, p + 1, hi)
    return arr


def med_part(arr, lo, hi):
    global comps
    mid = (lo + hi) // 2
    if arr[mid] < arr[lo]:
        arr[lo], arr[mid] = arr[mid], arr[lo]
    if arr[hi] < arr[lo]:
        arr[lo], arr[hi] = arr[hi], arr[lo]
    if arr[mid] < arr[hi]:
        arr[hi], arr[mid] = arr[mid], arr[hi]
    p = arr[hi]
    i = lo
    for j in range(lo, hi):
        comps += 1
        if arr[j] < p:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i


if __name__ == "__main__":
    sys.setrecursionlimit(100000)

    sizes = [10*x for x in range(1, 10)]
    sizes += [100*x for x in range(1, 10)]
    # sizes += [1000*x for x in range(1, 10 + 1)]
    
    last_qsort_comps = []
    med_qsort_comps = []
    for size in sizes:
        arr = np.arange(size)  # sorted asc array
        # arr = np.arange(size - 1, -1, -1)  # sorted desc array
        np.random.shuffle(arr) # random array

        # last_qsort
        comps = 0
        last_qsort(arr.copy(), 0, size - 1)
        last_qsort_comps.append(comps)
        
        # med_qsort
        comps = 0
        med_qsort(arr.copy(), 0, size - 1)
        med_qsort_comps.append(comps)
    plt.plot(sizes, last_qsort_comps, color="tab:orange", linestyle="solid", marker=".", label="last_qsort")
    plt.plot(sizes, med_qsort_comps, color="tab:cyan", linestyle="solid", marker=".", label="med_qsort")

    xs = np.array(sizes)

    # ys = 0.5*xs**2
    # plt.plot(xs, ys, color="tab:red", linestyle="dashed", label="O(n²)")

    ys = xs*np.log2(xs)
    plt.plot(xs, ys, color="tab:blue", linestyle="dashed", label="O(nlogn)")

    plt.title("Unsorted array")

    plt.xlabel("Array size")
    plt.ylabel("Comparisons")

    plt.xscale("log")

    plt.legend()
    plt.show()
