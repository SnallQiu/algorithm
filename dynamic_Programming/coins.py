#给你5，2，1分硬币，算出所有组合100分的组合情况的和
l = [50,25,10,5,1]
all_num = 100
def account(l,all):
    if all == 0 :
        return 1
    elif all < 0 or not l:
        return 0
    else:
        return account(l[1:], all) + account(l,all-l[0])


print(account(l, all_num))