def MAX_heapify(list,length,root):                 #使父节点大于子节点
    left = root*2 +1
    right = left + 1
    larger = root
    if right<length and list[right] > list[larger]:
        larger = right
    if left<length and list[left] > list[larger]:
        larger = left
    if larger!=root:
        list[larger],list[root] = list[root],list[larger]
        #MAX_heapify(list,length,larger)

def build_heap(list,length):                        #建堆
    for i in range((length-2)//2,-1,-1):            #//2 向下取整，从后往前
        MAX_heapify(list,length,i)

def sort(list):
    for i in range(len(list)-1,-1,-1):
        build_heap(list,i+1)
        list[0],list[i] = list[i],list[0]
    return list

import random
a = [random.randint(1,1000) for i in range(1000)]
print(a)
print(sort(a))

