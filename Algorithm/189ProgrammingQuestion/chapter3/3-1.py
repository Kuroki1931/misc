# 一つの配列を使って３つのstackを作る。

class triple_stack:
    def __init__(self):
        self.list_size = 100
        self.stack_size = 3
        self.list = [None] * self.list_size * self.stack_size

    def push(self, stack_num, value):
        if (stack_num == 1) | (stack_num == 2) | (stack_num == 3):
            for i in range(self.list_size * (stack_num - 1),  self.list_size * stack_num):
                if self.list[i] == None:
                    self.list[i] = value
                    break
        else:
            return 'no stack'

    def pop(self, stack_num):
        if (stack_num == 1) | (stack_num == 2) | (stack_num == 3):
            for i in range(self.list_size * (stack_num - 1),  self.list_size * stack_num)[::-1]:
                if self.list[i] != None:
                    pop_value = self.list[i]
                    self.list[i] = None
                    return pop_value
        else:
            return 'no stack'
