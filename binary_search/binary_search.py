# -- coding: utf-8 --
# author: snall  time: 2018/2/6

def binary(a,target):
    low = 0
    high = len(a)-1
    while low <=high:
        mid = (low+high)//2
        mid_num = a[mid]
        if mid_num == target:
            return mid
        elif mid_num > target:
            high = mid-1
        elif mid_num < target:
            low = mid+1
    return -1

a = [2,3,4,]
target = 4
print('第%d个'%(binary(a,target)+1))