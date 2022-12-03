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
l.append(3)
l.append(2)
l.append(7)
l.append(5)
l.append(4)
l.append(9)
l.append(8)
l.append(3)
l.append(4)

# 最終ノードを第4ノードに連結
l.head.next.next.next.next.next.next.next.next.next = l.head.next.next.next


# 解答
# loopしているか否かを判定。
# 配列リストを使ったが、メモリが増えるため作らない解答の方が望ましい。
def check_loop(l):
    front = l.head
    loop_list = []
    while front:
        if front not in loop_list:
            loop_list.append(front)
            front = front.next
        else:
            return True
    return False

# 初めのノードを特定する。


def get_value_start_loop(l):
    front = l.head
    loop_list = []
    while front not in loop_list:
        loop_list.append(front)
        front = front.next
    return front


"""
解答参照後
"""

# kと2kの速度で動くポインタを作る
# 衝突場所を特定する
# kを先頭に戻す。
# 衝突箇所を特定する。


def get_loop_start(self):
    slow = self.head
    fast = self.head

    while (slow != None) & (fast != None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if (slow == None) | (fast == None):
        return False

    slow = self.head

    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
