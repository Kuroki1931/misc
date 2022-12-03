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


# 解答
# リスト内で、指定した値より小さな値を前に持ってくる
# linkedlist -> linkedlist
# [1, 3, 7, 2, 8, 10, 3] 5 -> [1, 3, 2, 3, 7, 5, 8, 10]

def takefront_under_k_value(l, k):
    # 配列リストにする
    value_list = []
    front = l.head
    while front:
        value_list.append(front.value)
        front = front.next
    
    if k not in value_list:
        front = [i for i in value_list if i < k]
        rear = [i for i in value_list if i > k]
        value = front + [k] + rear
    
    else:
        front = [i for i in value_list if i < k]
        middle = [i for i in value_list if i == k]
        rear = [i for i in value_list if i > k]
        value =front + middle + rear
    
    # 連結リストに戻す
    s = LinkedList()
    for i in value:
        s.append(i)
        
    return s.show()


# 計算量　O(文字の長さ)


"""
解答参照後
"""
# ２つのlinkedlistを作ってくっつける
def takefront_under_kvalue(l, k):
    before = LinkedList()
    after = LinkedList()
    
    front = l.head
    while front:
        if front.value < k:
            before.append(front.value)
        else:
            after.append(front.value)
        front = front.next
    
    if before.head.value == None:
        return after.show()
    else:
        top = before.head
        while top.next != None:
            top = top.next
        top.next = after.head
        return before.show()





