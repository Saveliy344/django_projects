from Hash import *
from random import randint
import time


def best_hash_functions():
    def hash1(object):
        return 0

    def hash2(object):
        if isinstance(object, int):
            return object - int(not (object // 2))
        else:
            return len(str(object)) + int(not (len(str(object)) // 2))

    return hash1, hash2


def average_hash_functions():
    def hash1(object):
        return len(str(object)) ** 2

    def hash2(object):
        sum = 0
        for i in str(object):
            sum += ord(i)
        return sum + int(not (sum % 2))

    return hash1, hash2


def worse_hash_functions():
    def hash1(object):
        return 1

    def hash2(object):
        return 3

    return hash1, hash2


nodes = [randint(0, 2 ** 20) for i in range(2 ** 15)]
# print(nodes)
dif = 10
lengths = []
times = []
ht = Hash_table(11, *best_hash_functions(), max_fill=1)
for i in range(2 ** 5, 2 ** 10):
    ht.add([nodes[i], nodes[i]])
    if i % dif == 0:
        timer_begin = time.perf_counter()
    ht.get_sorted_list()
    if i % dif == 0:
        timer_end = time.perf_counter()
        if timer_end - timer_begin < 0.00015:
            lengths.append(i)
            times.append(timer_end - timer_begin)
list_times_lenghts = []
for i in range(len(lengths)):
    list_times_lenghts.append((lengths[i], times[i]))
for i in list_times_lenghts:
    print(f"({i[0]}; {i[1]})")

# Хеш-таблица
# Вставка лучший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *best_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.add([counter, counter * 2])
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
#
# # Поиск лучший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *best_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.find(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
# # Удаление лучший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *best_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.delete(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')

# Вставка средний случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *average_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.add([counter, counter * 2])
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths)
#     print(times)

# Поиск средний случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *average_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.find(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
#
# # Удаление средний случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *average_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.delete(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
# #
# # Вставка худший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *worse_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.add([counter, counter * 2])
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
#
# # Поиск худший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *worse_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.find(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
#
# # Удаление худший случай
# for fill in [50, 75, 99]:
#     lengths = []
#     times = []
#     print(f'============== Заполненность таблицы: {fill} ========================')
#     length_pows = [i for i in range(10, 15)]
#     for length_pow in length_pows:
#         counter = 1
#         ht = Hash_table(length_pow, *worse_hash_functions(), max_fill=1)
#         while ht.current_fill < fill / 100:
#             ht.add([counter, counter * 2])
#             counter += 2
#         timer_begin = time.perf_counter()
#         ht.delete(counter - 2)
#         timer_end = time.perf_counter()
#         lengths.append(2 ** length_pow)
#         times.append(timer_end - timer_begin)
#     print(lengths, times, sep='\n')
