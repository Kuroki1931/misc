import numpy as np

# 二分木が二分探索木であるかどうか判定する関数を作る
# テスト

# 二分探索木


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, val):
        if val <= self.value:
            if self.left:
                self.left.add(val)
            else:
                self.left = BinaryNode(val)
        else:
            if self.right:
                self.right.add(val)
            else:
                self.right = BinaryNode(val)


tree = BinaryNode(10)
tree.add(6)
tree.add(15)
tree.add(2)
tree.add(8)
tree.add(11)
tree.add(18)

#      10
#    6    15
# 2     8 11 18

# 二分探索木出ない


class treeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#         8
#    4         9
#  1   12    6   11


s = treeNode(8)
s.left = treeNode(4)
s.left.left = treeNode(1)
s.left.right = treeNode(12)
s.right = treeNode(9)
s.right.left = treeNode(6)
s.right.right = treeNode(11)

# 解答


def take_tree_value(tree, sort_list):
    if tree == None:
        return
    else:
        take_tree_value(tree.left, sort_list)
        sort_list.append(tree.value)
        take_tree_value(tree.right, sort_list)

    return sort_list


def check_tree(tree):
    sort_list = take_tree_value(tree, [])

    for i in range(len(sort_list)-1):
        if sort_list[i] > sort_list[i+1]:
            return False
    return True


# test
assert check_tree(tree) == True, 'error'
assert check_tree(s) == False, 'error'


"""
解答参照後
"""


def check_bst(tree, min=-np.inf, max=np.inf):
    if tree == None:
        return True
    if tree.value >= max or tree.value <= min:
        return False
    leftisTrue = check_bst(tree.left, min, tree.value)
    rightisTrue = check_bst(tree.right, tree.value, max)
    return leftisTrue and rightisTrue
