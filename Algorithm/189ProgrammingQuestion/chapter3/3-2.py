# minを持つstackを作成する。
#　例
# 4 -> 4, 2 -> 4, 2, 5 ->
# 4 -> 4, 2 -> 4, 2 ->

class StackWithMin:
    def __init__(self):
        self.list = []
        self.min_list = []

    def push(self, value):
        self.list.append(value)
        if len(self.min_list) == 0:
            self.min_list.append(value)
        else:
            if value <= self.min_list[-1]:
                self.min_list.append(value)

    def pop(self):
        pop_value = self.list[-1]
        self.list = self.list[:-1]
        if self.min_list[-1] == pop_value:
            self.min_list = self.min_list[:-1]
        return pop_value

    def min(self):
        min_value = self.min_list[-1]
        return min_value
