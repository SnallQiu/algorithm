'''
     1
  2     3
4  5  6  7
        8 9
'''
class Tree():
    def __init__(self,left=0,right=0,data=0):
        self.data = data
        self.left = left
        self.right = right

class Btree(Tree):
    def qout(self,base_tree=0):                     #前序遍历
        if base_tree == 0:
            return
        print(base_tree.data)
        self.qout(base_tree.left)
        self.qout(base_tree.right)
    def hout(self,base_tree=0):                     #后序遍历
        if base_tree == 0:
            return
        self.hout(base_tree.left)
        self.hout(base_tree.right)
        print(base_tree.data)
    def mout(self,base_tree=0):                     #中序遍历
        if base_tree == 0:
            return
        self.mout(base_tree.left)
        print(base_tree.data)
        self.mout(base_tree.right)

tree8 = Btree(data=8)
tree9 = Btree(data=9)
tree4 = Btree(data=4)
tree5 = Btree(data=5)
tree6 = Btree(data=6)
tree7 = Btree(tree8,tree9,7)
tree2 = Btree(tree4,tree5,2)
tree3 = Btree(tree6,tree7,3)
tree1 = Btree(tree2,tree3,100)
print('前序')
tree1.qout(tree1)
print('后序')
tree1.hout(tree1)