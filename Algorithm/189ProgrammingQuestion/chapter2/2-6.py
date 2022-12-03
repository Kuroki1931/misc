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


# テスト用
l = LinkedList()

l.append('N')
l.append('o')
l.append('w')
l.append(' ')
l.append('I')
l.append(' ')
l.append('W')
l.append('o')
l.append('n')


# 解答
#　linkedlistが回文かどうか調べる
# linkedlist -> bool
# 配列リストを使ったが、メモリが増えるため作らない解答の方が望ましい。
def check_reverse_word(l):
    front = l.head
    word_list = []
    while front:
        if (front.value == ' ') | (front.value == '!') | (front.value == ',') | (front.value == '?'):
            front = front.next
        else:
            word_list.append(front.value.lower())
            front = front.next

    index = len(word_list) // 2
    for i in range(index):
        if word_list[i] != word_list[-i-1]:
            return False

    return True


"""
以下解答参照後
"""
# ひっくり返して比較する。


def word_reverse_is_word(self):
    # コピーを作る
    self_copy = LinkedList()
    front = self.head
    while front:
        self_copy.append(front.value)
        front = front.next

    # ひっくり返す関数
    def reverse_linkedlist(self):
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        return self

    self_copy = reverse_linkedlist(self_copy)

    front_original = self.head
    front_copy = self_copy.head

    while (front_original != None) & (front_copy != None):
        if front_original.value != front_copy.value:
            return False
        front_original = front_original.next
        front_copy = front_copy.next
    return True
