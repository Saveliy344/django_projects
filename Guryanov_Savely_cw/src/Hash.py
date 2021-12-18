from random import randint


def hash1(object):
    return len(str(object)) ** 2


def hash2(object):
    sum = 0
    for i in str(object):
        sum += ord(i)
    return sum + int(not (sum % 2))


class Hash_table:
    def __init__(self, size, hash1, hash2, max_fill=0.3):
        self.size = 2 ** size
        self.pairs = [[None, None] for i in range(self.size)]
        self.hash1 = hash1
        self.hash2 = hash2
        self.max_fill = max_fill
        self.current_fill = 0
        self.sorted_list = []

    def extension(self):
        self.current_fill = 0
        self.size *= 2
        old_pairs = self.pairs
        self.pairs = [[None, None] for i in range(self.size)]
        for pair in old_pairs:
            if pair[0] != None:
                self.add(pair)

    def find_hash(self, object):
        i = -1
        while 1:
            i += 1
            yield (self.hash1(object) + i * self.hash2(object)) % self.size

    def add(self, pair):
        get_hash = self.find_hash(pair[0])
        hash = next(get_hash)
        while self.pairs[hash][0] != None and self.pairs[hash][0] != pair[0]:
            hash = next(get_hash)
        self.pairs[hash] = pair
        self.current_fill += 1 / self.size
        if self.current_fill >= self.max_fill:
            self.extension()

    def delete(self, key):
        get_hash = self.find_hash(key)
        hash = next(get_hash)
        while self.pairs[hash][0] != key:
            if self.pairs[hash] == [None, None]:
                raise IndexError(key)
            hash = next(get_hash)
        self.current_fill -= 1 / self.size
        self.pairs[hash] = [None, 0]

    def find(self, key):
        get_hash = self.find_hash(key)
        hash = next(get_hash)
        while self.pairs[hash][0] != key:
            if self.pairs[hash] == [None, None]:
                return None
            hash = next(get_hash)
        return self.pairs[hash][1]

    def sort(self):
        for pair in self.pairs:
            if pair[0] != None:
                self.sorted_list.append(pair[0])
        Hash_table.quick_sort(self.sorted_list)

    def get_sorted_list(self):
        return self.sorted_list

    @staticmethod
    def partition(array, begin, end):
        pivot = begin
        for i in range(begin + 1, end + 1):
            if array[i] <= array[begin]:
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[begin] = array[begin], array[pivot]
        return pivot

    @staticmethod
    def quick_sort(array, begin=0, end=None):
        if end is None:
            end = len(array) - 1

        def _quicksort(array, begin, end):
            if begin >= end:
                return
            pivot = Hash_table.partition(array, begin, end)
            _quicksort(array, begin, pivot - 1)
            _quicksort(array, pivot + 1, end)

        return _quicksort(array, begin, end)

# if __name__ == '__main__':
#     size = int(input('Введите размер таблицы:'))
#     pow = 0
#     while 2 ** pow < size:
#         pow += 1
#     ht = Hash_table(2 ** pow, hash1, hash2)
#     for i in range(size):
#         key = input('Введите ключ: ')
#         value = input('Введите значение: ')
#         ht.add([key, value])
#     print('Хеш-таблица успешно заполнена! Введите -1 для выхода или ключ для получения значения!')
#     key = input()
#     while key != '-1':
#         print('==========================')
#         print('Ключ:', key)
#         print('Значение:', ht.find(key))
#         key = input()
#
# ht = Hash_table(2, hash1, hash2, 0.3)
# for i in [randint(0, 10000) for i in range(1000)]:
#     ht.add([i, i])
# ht.sort()
# print(ht.get_sorted_list())
