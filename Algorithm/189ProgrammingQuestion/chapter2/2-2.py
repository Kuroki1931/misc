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
# 単方向連結リストに置いて、後ろからk番目の要素を見つけるアルゴリズムを考える
# linkedList -> linkedList

def get_value_k_from_back(k, l):
    front = l.head
    
    # 文字列が0の時, 文字列が1のとき
    if (front.value == None) | (front.next == None):
        return l.show()
    
    # 文字列のカウント
    else:
        length = 0
        while front:
            length += 1
            front = front.next
        
        back_key = k % length
        front_key = length - back_key
        
        front = l.head
        for _ in range(front_key):
            front = front.next
        print(front.value)


# 計算量 O(文字列の長さ)　


"""
解答参照後
"""
# わからない。


l = LinkedList()
front = l.head
def get_value_last_k(k, front):
    
    if front == None:
        return 0
    
    index = get_value_last_k(k, front.next) + 1
    
    if index == k:
        print(str(k) + 'th to last node is ' + str(front.value))
        
    return index