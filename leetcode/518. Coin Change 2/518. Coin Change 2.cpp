
// https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gx763A3x9Pl
// Coin change

class Solution {
public:
    int change(int amount, vector<int>& coins) {

        cout << "amount : " << amount << endl;
        const int ncnt = coins.size();

        // one way: no coins.
        if (0 == amount) {
            return 1;
        }
        // no way to form a valid combination.
        if (0 == ncnt) {
            return 0;
        }
            
        vector<vector<int>> dp(ncnt, vector<int>(amount + 1, 0) );

        // populate the sum=0 columns, as we will always have an empty set for zero sum
        // first columns to be 0.
        for (int ni = 0; ni < ncnt; ni++) {
            dp[ni][0] = 1;
        }

        
        for (int ni = 0; ni < ncnt; ni++) {
            for (int nj = 1; nj <= amount; nj++) {
                int comb1 = 0;
                int comb2 = 0;
                if (ni > 0) {
                    // the cominations excluding current indexed coint.
                    comb1 = dp[ni - 1][nj];
                }
                if (coins[ni] <= nj) {
                    // plus the cominations including current indexed coint.
                    comb2 = dp[ni][nj - coins[ni] ] ;
                }
                dp[ni][nj] = comb1 + comb2;
            }
        }
        
//         for (int ni = 0; ni < ncnt; ni++) {
//             cout << "dp: ";
//             for (int nj = 0; nj <= amount; nj++) {
//                 cout << dp[ni][nj] << ", " ;
//             }
//             cout << endl;
//         }

        return dp[ncnt - 1][amount];
        
        
    }
};


