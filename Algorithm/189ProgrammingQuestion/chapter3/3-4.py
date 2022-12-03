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

    def length(self):
        front = self.head
        if front.value == None:
            return 0
        else:
            count = 0
            while front:
                count += 1
                front = front.next
            return count


# 以下解答
# 片方のstackに貯めつつ、先頭の一つだけもう片方のstackに置いておく。
class MyQueue():
    def __init__(self):
        self.one = Stack()
        self.two = Stack()

    def push(self, value):
        if self.two.length() == 0:
            self.two.push(value)
        else:
            self.one.push(value)

    def pop(self):
        self.two.pop()
        if self.one.length() == 0:
            pass
        else:
            self.two.push(self.one.head.value)
            self.one.head = self.one.head.next
