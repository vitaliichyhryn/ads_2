import random
import string
from matplotlib import pyplot as plt

class DoubleHash:
    def __init__(self, size, load_factor=0.6):
        self.size = get_left_prime(size * 2)
        self.count = 0
        self.buckets = [None] * self.size
        self.load_factor = load_factor

    def jenkins(self, key):
        hashcode = 0
        for byte in key.encode("ascii"):
            hashcode = (hashcode + byte) & 0xFFFFFFFF
            hashcode = (hashcode + (hashcode << 10)) & 0xFFFFFFFF
            hashcode = (hashcode ^ (hashcode >> 6)) & 0xFFFFFFFF
        hashcode = (hashcode + (hashcode << 3)) & 0xFFFFFFFF
        hashcode = (hashcode ^ (hashcode >> 11)) & 0xFFFFFFFF
        hashcode = (hashcode + (hashcode << 15)) & 0xFFFFFFFF
        return hashcode

    def h2(self, key):
        hashcode = 0
        for byte in key.encode("ascii"):
            hashcode += byte
        return 1 + (hashcode % (self.size - 1))

    def put(self, key, value):
        if (self.count / self.size) > self.load_factor:
            self.rehash()
        i = 0
        while True:
            index = (self.jenkins(key) + i * self.h2(key)) % self.size
            if self.buckets[index] is None:
                self.buckets[index] = (key, value)
                self.count += 1
                return self.buckets[index]
            i += 1

    def get(self, key):
        global comparisons
        i = 0
        while True:
            index = (self.jenkins(key) + i * self.h2(key)) % self.size
            comparisons += 1
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            i += 1

    def rehash(self):
        temp = self.buckets
        self.size = get_left_prime(self.size * 2)
        self.buckets = [None] * self.size
        self.count = 0
        for pair in temp:
            if pair is not None:
                self.put(pair[0], pair[1])


def get_left_prime(number):
    for i in range(number - 1, 0, -1):
        factors = 0
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                factors += 1
        if factors == 0:
            return i


def generate_hashtable(size):
    hashtable = DoubleHash(size)
    keys = []
    for i in range(size):
        key = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 16)))
        if key not in keys:
            value = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 64)))
            hashtable.put(key, value)
            keys.append(key)
    return hashtable, keys


if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000, 20000]
    # comparisons_arr = []
    # for size in sizes:
    #     hashtable, keys = generate_hashtable(size)
    #     random_key = random.choice(keys)
    #     comparisons = 0
    #     hashtable.get(random_key)
    #     comparisons_arr.append(comparisons)
    #     print(comparisons)
    # plt.title("Search time complexity")
    # plt.xlabel("Hashtable size")
    # plt.ylabel("Number of comparisons")
    # plt.scatter(sizes, comparisons_arr, color="tab:blue", marker='o', s=10)
    # plt.grid(True)
    # plt.legend()
    # plt.show()
    size = sizes[4]
    for i in range(0, 4):
        hashtable, keys = generate_hashtable(size)
        random_key = random.choice(keys)
        print("hashtable size: " + str(size))
        print("random key: " + random_key)
        comparisons = 0
        print("found value: " + hashtable.get(random_key))
        print("number of comparisons: " + str(comparisons))
