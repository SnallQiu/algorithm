#单链表转置
#脑袋巨疼型递归
def reverse_V1(node):
    if node.next==None:
        return node
    result = reverse_V1(node.next)
    node.next.next = node    #这两行相当于递归时候被锁住了，（延时）
    node.next = None         #在最后一个执行完后（达到递归终止条件后），才会依次释放，执行。
    return result

#SCIP版迭代
def reverse_V2(node):
    def iter(node,pop_out):
        if node==None:
            return pop_out
        tmp = node.next
        node.next = pop_out
        return iter(tmp,node)

    return iter(node,None)   #这个就相当于每次弹出一个指向之前迭代的节点，迭代的对象则是最新的节点头部