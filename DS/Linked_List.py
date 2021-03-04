class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

a = Node(5)
b = Node(6)
a.nextnode = b
b.prevnode = a
print(a.value)
print(b.value)
print(a.nextnode.value)










