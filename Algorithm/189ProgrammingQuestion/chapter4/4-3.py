import queue

# 深さDの２分探索木が与えられた時に同じ深さのノード同士の連結リストを作るアルゴリズム。
# 連結リスト


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = Element(None)

    def append(self, value):
        front = self.head
        if front.value == None:
            self.head = Element(value)
        else:
            while front.next != None:
                front = front.next
            front.next = Element(value)

    def delete(self, n):
        front = self.head
        if n == 0:
            self.head = self.head.next
        else:
            count = 0
            while count != n-1:
                front = front.next
                count += 1
            front.next = front.next.next

    def show(self):
        front = self.head
        while front:
            print(front.value)
            front = front.next

# 二分探索機


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


# 解答
def tree_to_list_dfs(tree, lists, level):
    if tree != None:
        if len(lists) == level:
            new_linked_list = LinkedList()
            new_linked_list.append(tree.value)
            lists.append(new_linked_list)
        else:
            linked_list = lists[level]
            linked_list.append(tree.value)
        print(tree.value)

        tree_to_list_dfs(tree.left, lists, level+1)
        tree_to_list_dfs(tree.right, lists, level+1)

        return lists


def tree_to_list_bfs(tree):
    list_list = []
    node_list = []
    if tree != None:
        node_list.append(tree)
    else:
        return 'no_value'

    while len(node_list) != 0:
        new_list = []
        new_linked_list = LinkedList()
        for i in node_list:
            if i != None:
                new_linked_list.append(i.value)
                new_list.append(i.left)
                new_list.append(i.right)
        list_list.append(new_linked_list)
        node_list = new_list

    return list_list
