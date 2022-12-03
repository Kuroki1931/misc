# 昇順になれべられたリストを、浅い二分探索木に変換する。
# list -> tree
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def list_to_tree(sort_list):
    if len(sort_list) == 0:
        return
    else:
        center_index = int(round(len(sort_list) / 2, 0))
        center_value = sort_list[center_index]
        left_list = sort_list[:center_index]
        right_list = sort_list[center_index+1:]
        n = Node(center_value)
        n.left = list_to_tree(left_list)
        n.right = list_to_tree(right_list)

    return n
