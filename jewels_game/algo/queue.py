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
