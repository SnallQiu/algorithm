//
//  main.cpp
//  背包问题
//
//  Created by 裘 on 2020/1/10.
//  Copyright © 2020 裘. All rights reserved.
//

#include <iostream>
#include <cmath>
using namespace std;
// c++ 全部变量只能初始化，不能赋值，所以不能再这里用memset
int w[4] = {2,1,3,2};
int v[4] = {3,2,4,2};
int W = 5;
int res = 0;
int dp[4+1][5+1];  // 记忆化数组，
int _iter(int i, int j){
    if(i==4)
        return 0;
    if(dp[i][j]!=-1)
        return dp[i][j];
    if(w[i]>j)
        return _iter(i+1, j);
    else{
        int res = max(_iter(i+1, j),_iter(i+1,j-w[i]) + v[i]);
        dp[i][j] = res;
        return res;
    }
}

int _traverse(int W){
    int res = 0;
    for(int i=4;i>0;i--){
        for(int j=W;j>0;j--){
            if(w[i-1] > j)
                dp[i-1][j] = dp[i][j];
            else{
                dp[i-1][j] = max(dp[i][j-w[i-1]] + v[i-1],
                                 dp[i][j]);
            }
            res = max(res, dp[i-1][j]);
        }
    }
    return res;
}

int main() {
    // insert code here...
//    memset(dp, -1, sizeof(dp));
//    cout << _iter(0,W);
    memset(dp, 0, sizeof(dp));
    cout << _traverse(W);
    
    return 0;
}
