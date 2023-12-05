# Copy over your a1_partc.py file here
#    Main Author(s):
#    Main Reviewer(s):


class Stack:
    def __init__(self, cap=10):
        self.stack = [None] * cap
        self.cap = cap
        self.size = 0

    def capacity(self):
        return self.cap

    def push(self, data):
        if self.size >= self.cap:
            self.cap = self.cap * 2
            newStack = [None] * self.cap
            for i in range(self.size):
                newStack[i] = self.stack[i]
            self.stack = newStack
        self.stack[self.size] = data
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("pop() used on empty stack")
        poppedVal = self.stack[self.size - 1]
        self.stack[self.size - 1] = None
        self.size -= 1
        return poppedVal

    def get_top(self):
        if self.is_empty():
            return None
        return self.stack[self.size - 1]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


class Queue:
    def __init__(self, cap=10):
        self.cap = cap
        self.size = 0
        self.queue = [None] * cap

    def capacity(self):
        return self.cap

    def enqueue(self, data):
        if self.size >= self.cap:
            self.cap *= 2
        newQueue = [None] * self.cap
        for i in range(self.size):
            newQueue[i] = self.queue[i]
        self.queue = newQueue
        self.queue[self.size] = data
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue() used on empty queue")
        item = self.queue[0]
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]
        self.queue[self.size - 1] = None
        self.size -= 1
        return item

    def get_front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


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
