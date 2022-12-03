# Stack
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


# Queue
class Queue():
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
        print(self.head.value)
        self.head = self.head.next

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
