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

# 猫と犬を保護する施設を想定してアルゴリズムを実装する。
# enqueue 猫or犬を施設に入れる。
# dequeueAny 猫or犬で最も施設に長くいる動物を取り出す
# dequeueDog 犬で最も施設に長くいる動物を取り出す
# dequeueCat 猫で最も施設に長くいる動物を取り出す


class dog_cat_queue():
    def __init__(self):
        self.name_list = []
        self.species_list = []

    def enqueue(self, name, species):
        self.name_list.append(name)
        self.species_list.append(species)

    def dequeueAny(self):
        if len(self.species_list) == 0:
            return print('no animal')
        else:
            print(self.name_list[0], self.species_list[0])
            self.name_list = self.name_list[1:]
            self.species_list = self.species_list[1:]

    def dequeueDog(self):
        if 'dog' not in self.species_list:
            return print('no dog')
        else:
            for i, v in enumerate(self.species_list):
                if v == 'dog':
                    print(self.name_list[i], self.species_list[i])
                    self.name_list = self.name_list[:i] + self.name_list[i+1:]
                    self.species_list = self.species_list[:i] + \
                        self.species_list[i+1:]
                    break

    def dequeueCat(self):
        if 'cat' not in self.species_list:
            return print('no cat')
        else:
            for i, v in enumerate(self.species_list):
                if v == 'cat':
                    print(self.name_list[i], self.species_list[i])
                    self.name_list = self.name_list[:i] + self.name_list[i+1:]
                    self.species_list = self.species_list[:i] + \
                        self.species_list[i+1:]
                    break
