import numpy as np


class Element():
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self):
        self.head = Element(None)

    def push(self, value):
        front = self.head
        if front.value == None:
            self.head = Element(value)
        else:
            while front.next != None:
                front = front.next
            front.next = Element(value)

    def pop(self):
        front = self.head
        if front.next == None:
            print(front.value)
            self.head = Element(None)
        else:
            while front.next.next != None:
                front = front.next
            print(front.next.value)
            front.next = front.next.next

    def show(self):
        front = self.head
        while front:
            print(front.value)
            front = front.next

    def peek(self):
        front = self.head
        if front.value == None:
            return np.nan
        elif front.next == None:
            return front.value
        else:
            while front.next.next != None:
                front = front.next
            return front.next.value

# 解答
# stackをソートする関数を作る
# stack -> stack
# listの使用は不可であったが使用してしまった。


def stack_sort(l):
    each_value_list = []
    front = l.head
    while front:
        each_value_list.append(front.value)
        front = front.next

    change = True
    while change:
        change = False
        for i in range(len(each_value_list)-1):
            if each_value_list[i] > each_value_list[i+1]:
                each_value_list[i], each_value_list[i +
                                                    1] = each_value_list[i+1], each_value_list[i]
                change = True

    s = Stack()
    for l in each_value_list:
        s.push(l)

    return s


"""
解答参照後
"""
# もう一つstackを作成し、popした値でサイズを比べる動作を繰り返す。


def sort(l):
    r = Stack()
    while l.head.value != None:
        value = l.peek()
        l.pop()
        while (r.head.value != None) & (r.peek() < value):
            l.push(r.peek())
            r.pop()
        r.push(value)

    while r.head.value != None:
        sort_value = r.peek()
        r.pop()
        l.push(sort_value)

    return l
