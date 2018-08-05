#cookbook p118

class Node:
    def __init__(self,value):
        self.value = value
        self.child = []

    def __repr__(self):
        return 'Node({})'.format(self.value)
    def __iter__(self):
        return iter(self.child)
    def add_child(self,*args):
        for i in args:
            self.child.append(i)
    def depth_list(self):
        yield self
        for c in self:#因为有__iter__所以是个可迭代实例
            yield from c.depth_list()


root = Node(1)
child1 = Node(2)
child2 = Node(3)
root.add_child(child1,child2)
child1.add_child(Node(4),Node(5))
child2.add_child(Node(6))

for c in root.depth_list():
    print (c)

