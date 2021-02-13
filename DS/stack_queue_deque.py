class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


s = Stack()

print(s.isEmpty())
print(s.size())
s.push(1)
print(s.peek())


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, i):
        self.items.insert(0, i)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.iitems == []


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.items)


class Deque():
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def addFront(self, i):
        self.items.append(i)

    def addRear(self, i):
        self.items.insert(0, i)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)





