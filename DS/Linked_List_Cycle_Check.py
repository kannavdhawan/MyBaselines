class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

    def cycle_check(self, node):
        self.list = [node]
        self.set = {node}

        while len(self.list) == len(self.set) and node.nextnode != None:
            self.list.append(node.nextnode)
            self.set.add(node.nextnode)
            node = node.nextnode

            if len(self.list) != len(self.set):
                return True
        return False

a = Node(5)
b = Node(6)
c = Node(7)
d = Node(8)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = a
             ## Cycle Exists

print("Cycle Exists:",format(a.cycle_check(a)))