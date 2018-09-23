#最大和子矩阵
#时间复杂度 O(m*m*n)

a=[[1,2,3,5],
   [2,-34,6,3],
   [9,-13,4,4],
   [8,8,1,-2]]

n=4
m=4
all_max = 0
for i in range(m):
    sum_ = [0] * n
    for j in range(i,m):
        all = 0
        for k in range(n):
            sum_[k] += a[j][k]   #关键是这里将每行按列加起来，这样就能弄成一维数组，运用扫描算法（动态规划）
            all = all+sum_[k]
            all = max(all,0)     #动态规划，比0小就重新从0开始
            all_max = max(all_max,all)

print (all_max)
