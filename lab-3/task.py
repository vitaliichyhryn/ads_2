import sys


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

def read_arr(path):
    with open(path) as file:
        lines = file.readlines()
        return int(lines[0]), [int(line) for line in lines[1:]]


if __name__ == "__main__":
    args = sys.argv[1:]
    arr_len, arr = read_arr(args[0])
    print(f"input: {arr}")
    with open("output.txt", mode="w") as file:
        comps = 0
        print(f"last_qsort: {last_qsort(arr.copy(), 0, arr_len - 1)}")
        file.write(f"{comps} ")
        comps = 0
        print(f"med_qsort: {med_qsort(arr.copy(), 0, arr_len - 1)}")
        file.write(f"{comps} _")
