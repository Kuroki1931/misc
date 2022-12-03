import collections

# プロジェクトの依存関係。
"""
in: (a, b)  out: b, a  tree: a <- b
in: (a, b) (b, c)  out: c, b, a   tree: a <- b <- c

グラフ
自分に伸びている矢印がない、またはすでに実行されていれば実行することができる。
連結関係を表現する。->　上に該当するノードを実行&グラフから消去。-> 繰り返す。
"""

# 解答
input_data = ['a', 'b', 'c', 'd', 'e', 'f']
relation = [('d', 'a'), ('b', 'f'), ('d', 'b'), ('a', 'f'), ('c', 'd')]


class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []
        self.visited = False

    def add(self, node):
        self.adjacent.append(node)


def make_graph(input_data, relation):
    work_dic = {}
    for i in input_data:
        work_dic[i] = Node(i)

    for i in relation:
        node = work_dic[i[0]]
        node.add(i[1])

    return work_dic


def to_do_work(input_data, relation):
    if len(input_data) == 0:
        return []
    else:
        work_dic = make_graph(input_data, relation)

        work_list = []
        for x, y in zip(work_dic.keys(), work_dic.values()):
            if len(y.adjacent) == 0:
                work_list.append(x)

        new_input_data = []
        new_relation = []
        for i in input_data:
            if i not in work_list:
                new_input_data.append(i)

        for i in relation:
            if i[1] not in work_list:
                new_relation.append(i)

        print(work_list)
        print(len(new_input_data))
        print(new_relation)
        work_list += to_do_work(new_input_data, new_relation)

    return work_list


work_list = to_do_work(input_data, relation)


# 模範解答ぽく書くと


# 参照後
# Kahn’s algorithm
def topological_sort_bfs(graph):
    # トポロジカルソートした結果を蓄積する空リスト
    topological_sorted_list = []
    queue = collections.deque()
    # 入力辺を持たないすべてのノードの集合
    for vertex in graph:
        indegree = vertex.get_indegree()
        if indegree == 0:
            queue.append(vertex)
    # while S が空ではない do
    while len(queue) > 0:
        # S からノード n を削除する
        current_vertex = queue.popleft()
        # L に n を追加する
        topological_sorted_list.append(current_vertex.get_vertex_id())
        # for each n の出力辺 e とその先のノード m do
        for neighbor in current_vertex.get_connections():
            # 辺 e をグラフから削除する
            neighbor.set_indegree(neighbor.get_indegree() - 1)
            # if m がその他の入力辺を持っていなければ then
            if neighbor.get_indegree() == 0:
                # m を S に追加する
                queue.append(neighbor)
    if len(topological_sorted_list) != len(graph.get_vertices()):
        print("Kahn's algorithm:", '閉路があります。DAGではありません。')
    else:
        print("Kahn's algorithm tological sorted list:", topological_sorted_list)


# 深さ優先探索トポロジカルソート
def topological_sort_dfs(graph):
    # L ← トポロジカルソートされた結果の入る空の連結リスト
    topological_reverse_sorted_list = []
    try:
        # for each ノード n do
        for current_vertex in graph:
            # if n に permanent の印が付いていない then
            if not(current_vertex.permanent):
                topological_sort_dfs_visit(
                    current_vertex, topological_reverse_sorted_list)
    # 閉路を発見した場合
    except GraphTopologicalError:
        print('DFS algorithm:', '閉路があります。DAGではありません。')
    else:
        # リストは最後から読み出す
        print("DFS algorithm tological sorted list:",
              topological_reverse_sorted_list[::-1])


def topological_sort_dfs_visit(vertex, topological_sorted_list):
    if vertex.permanent:
        return
    # if n に「一時的」の印が付いている then
    if vertex.temporary:
        # 閉路があり DAG でないので中断
        raise GraphTopologicalError(topological_sorted_list)
    # n に「一時的」の印を付ける
    vertex.temporary = True
    # for each n の出力辺 e とその先のノード m do
    for neighbor in vertex.get_connections():
        topological_sort_dfs_visit(neighbor, topological_sorted_list)
    vertex.temprary = False
    # n に「恒久的」の印を付ける
    vertex.permanent = True
    # n を L に追加
    topological_sorted_list.append(vertex.get_vertex_id())
