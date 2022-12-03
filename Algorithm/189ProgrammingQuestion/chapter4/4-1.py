# 有効グラフが与えられた時に、２つのノードの間に経路があるかどうかを判定する。
# graph -> list

# BFS
import queue


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adjacent = []

    def add(self, node):
        self.adjacent.append(node)


n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")

n1.adjacent = [n2, n5, n6]
n2.adjacent = [n4, n5]
n3.adjacent = [n2]
n4.adjacent = [n3, n5]


def search_way(node1, node2):
    q = queue.Queue()
    node1.visited = True
    q.put(node1)

    while q.empty() == False:
        node = q.get()
        for n in node.adjacent:
            if n.visited == False:
                if n == node2:
                    return True
                n.visited == True
                q.put(n)
    return False


# テスト
assert search_way(n1, n4) == True, 'error'
