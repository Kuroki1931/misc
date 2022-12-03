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
l.append('a')
l.append('b')
l.append('c')
l.append('d')
l.append('e')


# 解答
# cにアクセスし削除をする。
# linkedlist -> linkedlist
def delete(l):
    if (l.head.value == None) or (l.head.next == None):
        return False
    else:
        l.head.next.next = l.head.next.next.next
        
    return l.show()