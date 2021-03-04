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


class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(10)
b = Node(20)
c = Node(30)
a.next_node = b
b.next_node = c

print("Value of A is {}".format(a.value))
print("Value of next node of A is {}".format(a.next_node.value))
print("Value of next node of B is {}".format(b.next_node.value))


class DoublyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


x = DoublyLinkedListNode(10)
y = DoublyLinkedListNode(20)
z = DoublyLinkedListNode(30)

x.next_node = y
y.prev_node = x
y.next_node = z
z.prev_node = y

print("X is {}".format(x.value))
print("Next Node of X is {}".format(x.next_node.value))
print("Previous Node of Y is {}".format(y.prev_node.value))
print("Next node of Y is {}".format(y.next_node.value))



