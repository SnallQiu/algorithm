import random
def quicksort(l,u):
    if l >= u:
        #最多一个元素，递归结束条件
        return
    t = x[l]
    s = l
    for i in range(l+1, u+1):
        if x[i] < t:
            # ++s
            s += 1
            # swap(s,i)
            tmp = x[s]
            x[s] = x[i]
            x[i] = tmp

    #swap(l,s)
    x[l] = x[s]
    x[s] = t

    quicksort(l, s-1)
    quicksort(s+1, u)


if __name__ == "__main__":
    x=[random.randint(1,100) for _ in range(100)]
    quicksort(0,len(x)-1)
    print(x)
