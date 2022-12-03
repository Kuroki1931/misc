# 一定の積み上げがなされたら新しいstack構造を作るclassを作成する。
# classの作成
# 5こ積み上げたら新しいstackを作るとする。
# 例　[1, 2, 3, 4, 5] -> [6, 7, 8, 9, 10] -> [11, 12, 13]
# 以下解答

# まずは単体のstackを作る。

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


# 解答
# リストを使ってstackを条件に応じて出し入れする。
class SetOfStacks():
    def __init__(self):
        self.start = Stack()
        self.list = [self.start]

    def push(self, value):
        # リストの最後のstackを取り出す。
        stack_list = self.list
        last_stack_index = len(stack_list) - 1
        last_stack = self.list[last_stack_index]
        # リストの長さが5以下ならそのstackに加える。
        if last_stack.length() < 5:
            last_stack.push(value)
        # 5以上であれば新しく作って追加及びリストに足す。
        else:
            s = Stack()
            s.push(value)
            self.list.append(s)

    def pop(self):
        # リストの最後のstackを取り出す。
        stack_list = self.list
        last_stack_index = len(stack_list) - 1
        last_stack = self.list[last_stack_index]
        # リストの長さが0以上ならそのstackから取り出す。
        if last_stack.length() > 0:
            last_stack.pop()
        # 0で最後のstackを消して、一つ前のstackから取り出す。
        else:
            self.list = self.list[:last_stack_index]
            stack_list = self.list
            last_stack_index = len(stack_list) - 1
            last_stack = self.list[last_stack_index]
            last_stack.pop()
