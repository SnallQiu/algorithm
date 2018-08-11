'''动态规划 题目1
一个列表，找出和最大的连续队列，并返回最大值以及该队列
a = [1,-2,3,4,5,2,-10,6,7]
return
    [3,4,5,2,-10,6,7] 17
'''
a = [1, -2, 3, 4, 5, 2, 0, -20, 6, 7]

class DP1:
    def dp(self,a):
        maps_list = []
        temps=[]
        Max , temp = a[0] , 0#temp即为临时的最大值,如果小于0说明前面的那些都不需要了，直接替换新起点
        for index,i in enumerate(a,0):
            temps.append(i)
            if temp < 0 :
                temp = i
                temps=[i]
            else:
                temp += i
                temp_ = temps[:]#这里需要新建一个列表，不然temp一直改变，填进去的maps_list也会改变
                maps_list.append((temp,temp_))
            Max = max(Max,temp)
        for result in maps_list[::-1]:
            if result[0]==Max:
                print (result[1],Max)
                return result[1],Max


dp=DP1()
dp.dp(a)




