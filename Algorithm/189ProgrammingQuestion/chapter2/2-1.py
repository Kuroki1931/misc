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

# 連結リストから重複がある文字を消去する。
# list -> list
# ['a', 'b' 'c'] -> ['a', 'b' 'c']
# ['a', 'b' 'c', 'a', 'x'] -> ['a', 'b' 'c', 'a', 'x']


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)


# 解答
def delete_duplicate(l):
    front = l.head
    setList = []
    s = LinkedList()

    while front:
        if front.value not in setList:
            setList.append(front.value)
            s.append(front.value)
        front = front.next
    return s.show()

# 計算時間　O(文字の長さ)


"""
解答参照後
"""
# ２つに分ける
# メモリなしの場合


def delete_duplicate(l):
    front = l.head
    while front != None:
        runner = front
        while runner.next != None:
            if runner.next.value == front.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        front = front.next
    return l.show()

# 計算量　O(n^2)    消費メモリO(1)
