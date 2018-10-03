def parttion(v,left,right):
    key = v[left]                                         #指定基数 即这堆数列最左边的数
    low = left
    high = right
    while low < high:
        while (low < high) and v[high]>=key:              #从右往左扫，直到找到一个比基数小的数
            high -= 1
        v[low] = v[high]                                  #将这个数赋给最左边的数
        while (low < high) and v[low]<=key:               #从左往右扫，直到找到一个比基数大的数
            low += 1
        v[high] = v[low]                                  #把这个数赋给上面那个找的数
        v[low] = key                                      #基数赋给这个数
    return low                                            #循环这个过程，使基数的右边都大于他左边都小于他
def quicksort(v,left,right):
    if left < right:
      p = parttion(v,left,right)                          #分成两堆后，将这两堆循环这个过程，直到排序完成

      #Q：编程珠玑习题，O(N)内，查找第k个小的数
      #A：思路是下面两行递归时候加上判断
      # if p>k-1: quciksort(v,p+1,right) if p<k-1:quciksort(v,left,p-1) ,if p==k-1:return v[k-1]
      #不需要全部递归完排序，只需要判断k右边都比他大，k左边都比他小，就结束。
      quicksort(v,p+1,right)
      quicksort(v,left,p-1)
    return v

a = [1,3222222,2,5,77,88,99,11,22,445,6,7,888,999,556]
print(quicksort(a,0,len(a)-1))

