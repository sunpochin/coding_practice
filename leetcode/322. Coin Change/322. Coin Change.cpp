// https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/NE0yNJ1rZy6

// class Solution {

//     public:
//     int coinChange(vector<int>& coins, int amount) {
        
//         int sumall = this->coinRecur(coins, amount, 0);
//         if (sumall >= 0 ) {
//             return sumall + 1;
//         } else {
//             return -1;
//         }
// //        return sumall;
//     }

// private:
//     int coinRecur(vector<int>& coins, int amount, int nidx) {
//         // base condition.
//         if (0 == amount) {
//             cout << "base condition: " << nidx << endl;
//             return nidx;
//         }
        
//         if (coins.empty() || nidx >= coins.size() ) {
// //            cout << "coin size error: nidx: " << nidx << ", coins.size(): " << coins.size() << endl;
//             return -1;
//         }
        
//         int sum1 = -1;
//         int sum2 = -1;
//         if (coins[nidx] <= amount) {
//             sum1 = coinRecur(coins, amount - coins[nidx], nidx );
// //            cout << "calculate sum1: " << sum1 << endl;
//         }

//         sum2 = coinRecur(coins, amount, nidx + 1);
// //        cout << "sum1: " << sum1 << ", sum2: " << sum2 << endl;
//         return max(sum1, sum2);
//     }


// };



class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        
        int nsize = coins.size();
        
        vector<vector<int> > dp(nsize, vector<int>(amount + 1) );
        for (int ni = 0; ni < nsize; ni++) {
            for (int nj = 0; nj <= amount; nj++) {
                dp[ni][nj] = numeric_limits<int>::max();
            }
        }
        
    // populate the total=0 columns, as we don't need any coin to make zero total
        for (int i = 0; i < nsize; i++) {
          dp[i][0] = 0;
        }
        
        
        for (int i = 0; i < nsize; i++) {
            for (int t = 1; t <= amount; t++) {
              // if (coins[i] > amount) 
                if (i > 0) {
                    // exclude the coins.
                    dp[i][t] = dp[i - 1][t];
                } 
                
                // include the coins.
                if (coins[i] <= t)  {
                    if (dp[i][t - coins[i] ] != numeric_limits<int>::max() ) {
                        dp[i][t] = min(dp[i][t], dp[i][t - coins[i] ] + 1);
                    }
                }
//                cout << "dp[" << i << "][" << t << "]: " << dp[i][t] << ", ";
            }
//            cout << endl;
        }

        return dp[nsize - 1][amount] == numeric_limits<int>::max() ? -1 : dp[nsize - 1][amount];
    }
};



