
class Deque:
    def __init__(self, cap=10):
        self.cap = cap
        self.queue = [None] * cap
        self.size = 0

    def capacity(self):
        return self.cap

    def increase_capacity(self):
        if self.size >= self.cap:
            self.cap *= 2

    def push_front(self, data):
        self.increase_capacity()
        newdequeu = [None] * self.cap
        newdequeu[0] = data
        for i in range(self.size):
            newdequeu[i + 1] = self.queue[i]
        self.queue = newdequeu
        self.size += 1

    def push_back(self, data):
        old_cap = self.cap
        self.increase_capacity()
        newdequeu = [None] * self.cap
        for i in range(self.size):
            newdequeu[i] = self.queue[i]
        newdequeu[self.size] = data
        self.queue = newdequeu
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError("pop_front() used on empty deque")
        item = self.queue[0]
        for i in range(1, self.size):
            self.queue[i - 1] = self.queue[i]
        self.size -= 1
        self.queue[self.size] = None
        return item

    def pop_back(self):
        if self.is_empty():
            raise IndexError("pop_back() used on empty deque")
        self.size -= 1
        item = self.queue[self.size]
        self.queue[self.size] = None
        return item

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def get_back(self):
        if self.is_empty():
            return None
        return self.queue[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def __getitem__(self, k):
        if k >= self.size:
            raise IndexError("Index out of range")
        return self.queue[k]
