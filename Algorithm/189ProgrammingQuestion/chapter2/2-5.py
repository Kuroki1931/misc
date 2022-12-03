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
m = LinkedList()
n = LinkedList()

m.append(7)
m.append(2)
m.append(4)

n.append(3)
n.append(4)
n.append(8)


# 解答
# 2つのlinkedlistの値を足し合わせる。
# linkedlist -> linkedlist
# 配列リストを使ったが、メモリが増えるため作らない解答の方が望ましい。

def get_add_value(m, n):
    m_front = m.head
    n_front = n.head

    # 数の取り出し
    m_value = 0
    m_index = 0
    while m_front:
        ten = 10 ** m_index
        parts_value = m_front.value * ten
        m_value += parts_value
        m_index += 1
        m_front = m_front.next

    n_value = 0
    n_index = 0
    while n_front:
        ten = 10 ** n_index
        parts_value = n_front.value * ten
        n_value += parts_value
        n_index += 1
        n_front = n_front.next

    add_value = m_value + n_value

    # linkedlistに戻す
    l = LinkedList()
    add_value = str(add_value)
    for i in range(len(add_value)):
        part = int(add_value[-i-1])
        l.append(part)

    return l.show()


# 発展問題
# 初めに文字列の長さを数えてからやればできる。


"""
解答参照後
"""

# 回帰による回答。
# for loopの中にresultを置いてreturn で返したいがうまくできない。
m_front = m.head
n_front = n.head
result = LinkedList()


def add_linkedlist(m_front, n_front, carry=0):

    if (m_front == None) & (n_front == None) & (carry == 0):
        return None
    else:
        if m_front != None:
            carry += m_front.value
        if n_front != None:
            carry += n_front.value

        setvalue = carry % 10
        result.append(setvalue)

        if (m_front != None) | (n_front != None):
            if m_front != None:
                m_front = m_front.next
            if n_front != None:
                n_front = n_front.next
            if carry >= 10:
                carry = 1
            else:
                carry = 0

            add_linkedlist(m_front, n_front, carry)
