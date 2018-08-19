#非递归版本，可以省空间 空间复杂度为o(N)
#只需要一个初始数组 不需要递归 根据数组的位排序。
#思路就是2个合并 然后4个合并 ....len(list)*log(len(list))次合并
import random
seq = [random.randint(1,100) for i in range(1,100)]

def merge(seq,low,mid,height):
    left = seq[low:mid]
    right = seq[mid:height]

    a=[]
    while len(left)>0 and len(right)>0:
        if left[0]<right[0]:
            a.append(left.pop(0))
        else:
            a.append(right.pop(0))
    a += left
    a += right

    seq[low:height] = a
    print(seq)



def main():
    print('origin:', seq)
    l = 1
    while l<len(seq):
        i = 0
        while i<len(seq):
            low = i
            mid = i+l
            height_temp = i+2*l
            height = min(height_temp,len(seq))
            if mid < height:
                merge(seq,low,mid,height)
            i = 2*l+i
        l = l*2

    print ('after DC :',seq)

main()