# 連結リストを作る
class Element():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = Element(None)

    def append(self, value):
        new_element = Element(value)
        if self.head.value == None:
            self.head = new_element
        else:
            front = self.head
            while front.next != None:
                front = front.next
            front.next = new_element

    def show(self):
        front = self.head
        while front:
            print(front.value)
            front = front.next


l = LinkedList()
m = LinkedList()

l.append(3)
l.append(2)
l.append(7)
l.append(5)
l.append(4)
l.append(9)
l.append(8)
l.append(3)
l.append(4)

m.append(4)
m.append(3)
m.append(7)
m.append(9)

# lの5番目と連結
m.head.next.next.next.next = l.head.next.next.next.next


# 解答
# 配列リストを使ったが、メモリが増えるため作らない解答の方が望ましい。
def get_common_value(l, m):
    # 長さをカウント及びnodeを配列リストに入れる
    l_length = 0
    l_front = l.head
    l_list = []
    m_length = 0
    m_front = m.head
    m_list = []

    while l_front:
        l_length += 1
        l_list.append(l_front)
        l_front = l_front.next
    while m_front:
        m_length += 1
        m_list.append(m_front)
        m_front = m_front.next

    # 最後尾のメモリが異なる場合は共通の部分は存在しない。
    if l_front != m_front:
        return False

    # 長さに差がある場合は長い方を長い分削る
    difference = l_length - m_length
    if difference < 0:
        m_list = m_list[abs(difference):]
    elif difference > 0:
        l_list = l_list[abs(difference):]

    length = min(l_length, m_length)
    # 前から比べていき等しくなるノードを見つける
    for i in range(length-1):
        if m_list[i] == l_list[i]:
            return m_list[i+1:]
    return False


# 計算量　O(長さ+長さ）

"""
解答参照後
"""

# 2-6で使ったreverse関数を使えば、メモリを節約できる。
