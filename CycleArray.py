class CycleArray:
    def __init__(self, size=1):
        self.size = size
        self.arr = [None] * size
        self.start = 0  # 左闭右开，[start, end)，start指向第一个有效元素
        self.end = 0  # end指向最后一个有效元素的下一个位置
        self.count = 0  # the counter of the array

    def resize(self, newSize):
        new_arr = [None] * newSize
        for i in range(self.count):
            new_arr[i] = self.arr[(self.start+i) % self.size]
        self.arr = new_arr
        self.start = 0
        self.end = self.count
        self.size = newSize

    # 头部添加元素
    def add_first(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.start = (self.start - 1 + self.size) % self.size
        self.arr[self.start] = val
        self.count += 1

    # 尾部添加元素
    def add_last(self, val):
        if self.is_full():
            self.resize(self.size * 2)
        self.arr[self.end] = val
        self.end = (self.end + 1) % self.size
        self.count += 1

    # 头部删除元素
    def remove_first(self):
        if self.is_empty():
            raise Exception("The array is empty!")
        self.arr[self.start] = None
        self.start = (self.start + 1) % self.size
        self.count -= 1
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # 尾部删除元素
    def remove_last(self):
        if self.is_empty():
            raise Exception("The array is empty!")
        self.end = (self.end - 1 + self.size) % self.size
        self.arr[self.end] = None
        self.count -= 1
        if self.count > 0 and self.count == self.size // 4:
            self.resize(self.size // 2)

    # 获取头部元素
    def get_first(self):
        if self.is_empty():
            raise Exception("The array is empty!")
        return self.arr[self.start]

    def get_last(self):
        if self.is_empty():
            raise Exception("The array is empty!")
        return self.arr[(self.end - 1 + self.size) % self.size]

    def is_full(self):
        return self.count == self.size

    def is_empty(self):
        return self.count == 0

    def get_size(self):
        return self.count

a = CycleArray(6)
print(a.arr)
print(a.get_size())

a.add_first(0)
a.add_last(1)
a.add_first(2)
a.add_first(3)
a.add_last(4)
a.add_last(5)
print(a.arr)

a.remove_first()
a.remove_last()
print(a.arr)