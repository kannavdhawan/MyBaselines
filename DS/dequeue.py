class Dequeue:
    def __init__(self):
        self.items = []

    def addFront(self, element):
        self.items.append(element)

    def addRear(self, element):
        self.items.insert(0, element)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

dq = Dequeue()

dq.addRear(1)
dq.addRear(2)
dq.addRear(3)

print(dq.items)

dq.addFront(5)

print(dq.items)