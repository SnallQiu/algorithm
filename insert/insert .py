def insert(list):
    length = len(list)
    for i in range(1,length):
        if list[i]<list[i-1]:
            index = i                  #记录插入的位置
            value = list[i]            #记录插入的值
            while index>0 and list[index-1]>value:
                list[index] = list[index-1]
                index -= 1
            list[index] = value
    return list

list = [5,71,222,44,]
print(insert(list))