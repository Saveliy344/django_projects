from AVL import *
from random import randint
import time

nodes = [randint(0, 2 ** 20) for i in range(2 ** 15)]
# print(nodes)
dif = 10
lengths = []
times = []
avl = AVLTree()
for i in range(2**5, 2 ** 10):
    avl.insert(nodes[i])
    if i % dif == 0:
        timer_begin = time.perf_counter()
    avl.get_sorted_list()
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
# lengths = []
# times = []
# avl = AVLTree()
# for i in range(2 ** 15):
#     avl.insert(nodes[i])
#     if i % dif == 0:
#         timer_begin = time.perf_counter()
#     avl.find(nodes[i])
#     if i % dif == 0:
#         timer_end = time.perf_counter()
#         if timer_end - timer_begin < 0.00015:
#             lengths.append(i)
#             times.append(timer_end - timer_begin)
#
# lengths = []
# times = []
# avl = AVLTree()
# for i in range(2 ** 15):
#     avl.insert(nodes[i])
# for i in range(2 ** 15):
#     if i % dif == 0:
#         timer_begin = time.perf_counter()
#     avl.delete_value(nodes[i])
#     if i % dif == 0:
#         timer_end = time.perf_counter()
#         if timer_end - timer_begin < 0.00015:
#             lengths.append(i)
#             times.append(timer_end - timer_begin)
