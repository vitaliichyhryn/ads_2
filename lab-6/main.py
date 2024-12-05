import sys
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
    args = sys.argv[1:]
    arr = read_arr(args[0])
    medians = get_medians(arr)
    output = "\n".join(" ".join([str(median) for median in row]) for row in medians)
    with open("output.txt", mode="w") as file:
        file.write(output)
