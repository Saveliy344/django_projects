from Hash import Hash_table, hash1, hash2
from AVL import *


def test_hash_for_size():
    length_pows = [i for i in range(2, 7)]
    for length_pow in length_pows:
        ht = Hash_table(length_pow, hash1, hash2)
        right_values = []
        for i in range(2 ** length_pow):
            right_values.append(2 ** i - 3 * i + 5)
            ht.add([i, 2 ** i - 3 * i + 5])
        for i in range(2 ** length_pow):
            value = ht.find(i)
            assert value == right_values[i]
            ht.delete(i)
            assert ht.find(i) == None


def test_hash_for_max_fill():
    fills = [i for i in range(2, 10)]
    for fill in fills:
        ht = Hash_table(10, hash1, hash2, fill / 10)
        right_values = []
        for i in range(2 ** 10):
            right_values.append(2 ** i - 3 * i + 5)
            ht.add([i, 2 ** i - 3 * i + 5])
        for i in range(2 ** 10):
            value = ht.find(i)
            assert value == right_values[i]
            ht.delete(i)
            assert ht.find(i) == None


def preOrdertestTraverse(tree, node, preverse):
    if node is not None:
        preverse.append(node.value)
        preOrdertestTraverse(tree, node.left_child, preverse)
        preOrdertestTraverse(tree, node.right_child, preverse)


def test_for_AVL1():
    tree = AVLTree()
    for i in range(10):
        tree.insert(i)
    right_Traverse = [3, 1, 0, 2, 7, 5, 4, 6, 8, 9]
    preverse = []
    preOrdertestTraverse(tree, tree.root, preverse)
    assert preverse == right_Traverse


def test_for_AVL2():
    tree = AVLTree()
    for i in range(20):
        tree.insert(i)
    tree.delete_value(19)
    tree.delete_value(7)
    right_Traverse = [8, 3, 1, 0, 2, 5, 4, 6, 15, 11, 9, 10, 13, 12, 14, 17, 16, 18]
    preverse = []
    preOrdertestTraverse(tree, tree.root, preverse)
    assert preverse == right_Traverse


def test_for_AVL3():
    tree = AVLTree()
    for i in range(0):
        tree.insert(i)
    right_Traverse = []
    preverse = []
    preOrdertestTraverse(tree, tree.root, preverse)
    assert preverse == right_Traverse
