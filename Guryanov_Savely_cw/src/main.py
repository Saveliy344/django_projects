from AVL import *
from Hash import *
from random import randint
list_random = [randint(1, 100000) for i in range(1000)]


def hash_function():
    def hash_function1(object):
        return 0

    def hash_function2(object):
        if isinstance(object, int):
            return object + int(not (object // 2))
        else:
            return 1


avl = AVLTree()
ht = Hash_table()
sorted_hash = []
for i in list_random:
    if ht.find(i):
        ht.add([])