# -- coding: utf-8 --
# author: snall  time: 2018/2/24
import random
def shell_sort(a):
    step=len(a)//2
    while step:
        for i in range(step,len(a)):
            while i>=step and a[i-step]>a[i]:
                a[i-step],a[i] = a[i],a[i-step]
                i -= step
        step //= 2
    return a

a=[random.randint(1,1000)for i in range(1000)]
print(shell_sort(a))

