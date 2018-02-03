def divide(list):
    if len(list)==1:
        return list
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    #继续迭代细分 直到有一个元素分成一个

    ll = divide(left)
    rr = divide(right)

    return merge(ll,rr)

def merge(ll,rr):
    result = []
    while len(ll)>0 and len(rr)>0:
        if ll[0]<=rr[0]:
            result.append(ll.pop(0))
        else:
            result.append(rr.pop(0))
    #当有一个列表为空的时候 说明那个列表全放进去了，把剩下的另一个列表放到后面
    result +=ll
    result +=rr
    return result
import random
def test():
    a = [random.randint(1,1000) for x in range(1000)]
    print(a)
    print(divide(a))
test()
