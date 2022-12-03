# 二分探索木で与えられたノードの次のノードを検索するアルゴリズムを設計。
# 同じはない。

# 解答
def next_node(tree, node):
    if tree == None:
        return

    current_node = tree
    target_value = node.value
    while current_node:
        if current_node == None:
            return False
        elif current_node.value < target_value:
            current_node = current_node.right
        elif current_node.value > target_value:
            current_node = current_node.left
        else:
            break

    return current_node.left, current_node.right

    # 計算量 N(深さ）

    # 上の解答は与えられたノードのleft, rightの子供ノード。
    # 質問されている内容と異なる。


"""
解答参照後
"""


def most_left(node):
    if node == None:
        return
    else:
        while node.left != None:
            node = node.left
        return node


def next_node_inorder(tree, node):
    if tree == None:
        return

    current_node = tree
    target_value = node.value
    while current_node:
        if current_node == None:
            return False
        elif current_node.value < target_value:
            current_node = current_node.right
        elif current_node.value > target_value:
            current_node = current_node.left
        else:
            break

    if current_node.right != None:
        return most_left(current_node.right)
    else:
        parent = current_node.parent
        while (parent != None) & (parent.left != current_node):
            current_node = parent
            parent = parent.parent

        return parent
