class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,element):
        self.items.insert(0,element)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def IsEmpty(self):
        return len(self.items) == 0


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.items)