import timeit, math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial
from abc import ABC, abstractmethod


class HeapBase(ABC):
    def __init__(self):
        self.arr = []

    @property
    def size(self):
        return len(self.arr)

    @abstractmethod
    def heapify_down(self, parent):
        ...

    @abstractmethod
    def heapify_up(self, child):
        ...

    def pop(self):
        if self.arr:
            root = self.arr[0]
            last_leaf = self.arr.pop()
            if self.arr:
                self.arr[0] = last_leaf
                self.heapify_down(0)
            return root
        else:
            return None

    def push(self, key):
        self.arr.append(key)
        self.heapify_up(self.size - 1)

    def peek(self):
        if self.arr:
            return self.arr[0]
        else:
            return None


class MaxHeap(HeapBase):
    def heapify_down(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        largest = parent
        if left < self.size and self.arr[left] > self.arr[largest]:
            largest = left
        if right < self.size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != parent:
            self.arr[parent], self.arr[largest] = self.arr[largest], self.arr[parent]
            self.heapify_down(largest)

    def heapify_up(self, child):
        parent = (child - 1) // 2
        if child > 0 and self.arr[child] > self.arr[parent]:
            self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
            self.heapify_up(parent)


class MinHeap(HeapBase):
    def heapify_down(self, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        smallest = parent
        if left < self.size and self.arr[left] < self.arr[smallest]:
            smallest = left
        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right
        if smallest != parent:
            self.arr[parent], self.arr[smallest] = self.arr[smallest], self.arr[parent]
            self.heapify_down(smallest)

    def heapify_up(self, child):
        parent = (child - 1) // 2
        if child > 0 and self.arr[child] < self.arr[parent]:
            self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
            self.heapify_up(parent)


def get_medians(arr):
    min_heap = MinHeap()
    max_heap = MaxHeap()
    medians = []
    for num in arr:
        if min_heap.size == max_heap.size:
            max_heap.push(num)
            min_heap.push(max_heap.pop())
        else:
            min_heap.push(num)
            max_heap.push(min_heap.pop())
        if min_heap.size > max_heap.size:
            medians.append([min_heap.peek()])
        else:
            medians.append([max_heap.peek(), min_heap.peek()])
    return medians


def read_arr(path):
    with open(path) as file:
        lines = file.readlines()
        return [int(line) for line in lines[1:]]


if __name__ == "__main__":
    sizes = [10 * x for x in range(1, 10)]
    sizes += [100 * x for x in range(1, 10)]
    sizes += [1000 * x for x in range(1, 10 + 1)]
    sizes += [10000 * x for x in range(1, 10 + 1)]
    # sizes += [100000 * x for x in range(1, 10 + 1)]
    # sizes += [1000000 * x for x in range(1, 10 + 1)]
    times = []
    for size in sizes:
        arr = np.arange(size)  # sorted asc array
        np.random.shuffle(arr)  # random array
        times.append(timeit.timeit("get_medians(arr)", number=1, globals=globals()))

    plt.plot(sizes, times, color="tab:cyan", linestyle="solid", marker=".", label="get_medians")

    xs = np.array(sizes)

    ys = [sum([np.log2(x) * 0.000001 for x in range(1, size + 1)]) for size in sizes]
    plt.plot(xs, ys, color="tab:blue", linestyle="dashed", label="O(lgn!)")

    plt.title("Time Complexity")

    plt.xlabel("Input Size")
    plt.ylabel("Time")

    plt.xscale("log")
    plt.yscale("log")

    plt.legend()
    plt.show()
