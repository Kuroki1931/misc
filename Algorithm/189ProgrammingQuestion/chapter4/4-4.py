# 気が平衡可動化を調べる。差が1以下。
# 全ての木の深さを求めて計算する。


# 解答１
def check_tree_balance(tree, depth_list, level):
    if tree.left != None:
        check_tree_balance(tree.left, depth_list, level+1)
    else:
        depth_list.append(level)
    if tree.right != None:
        depth_list.append(level)
    return depth_list


# 解答2
def check_tree(tree):
    if tree == None:
        return -1
    return max(check_tree(tree.left), check_tree(tree.right)) + 1


def check_balance(tree):
    if tree == None:
        return True
    diff = check_tree(tree.left) - check_tree(tree.right)
    if abs(diff) > 1:
        return False
    else:
        return check_balance(tree.left) & check_balance(tree.right)

# 解答3
