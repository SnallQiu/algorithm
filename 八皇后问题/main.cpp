//
//  main.cpp
//  八皇后问题
//
//  Created by 裘 on 2020/1/12.
//  Copyright © 2020 裘. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;
int N = 8; // N皇后问题
int dp[8][8];
bool check(int x, int y){
    // check row
    for(int i=0; i<N; i++){
        if(i!=x&&dp[i][y]==1)
            return false;
    }
    // check left diagonal
    for(int i=x-1, j=y-1;i>=0&&j>=0;i--,j--){
        if(dp[i][j]==1)
            return false;
    }

    // check right diagnol;
    for(int i=x+1, j=y+1;i<N&&j<N;i++,j++){
        if(dp[i][j]==1)
            return false;
    }
    
    for(int i=x-1, j=y+1;i>=0&&j<N;i--,j++){
        if(dp[i][j]==1)
            return false;
    }
    
    for(int i=x+1, j=y-1;i<N&&j>=0;i++,j--){
        if(dp[i][j]==1)
            return false;
    }
    
    return true;
}

// x轴上从左到右。
int _iter(int n){
    int res = 0;
    if(n == N){
        res += 1 ;
    }
    else{
        for(int i=0; i<N; i++){
            if(check(n, i)){
                dp[n][i] = 1;
                res += _iter(n+1);
                dp[n][i] = 0;
            }
        }
    }
    return res;
}

int main(int argc, const char * argv[]) {
    memset(dp, 0, sizeof(dp));
    int count = _iter(0);
    cout << count << endl;
    return 0;
}
