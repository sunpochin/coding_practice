// https://leetcode.com/problems/fibonacci-number/submissions/
// https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gx6jmzrMwgZ/preview

class Solution {
public:
    int fib(int N) {
        vector<int> dp(N + 1, 0);
        if (N >= 0) {
            dp[0] = 0;
//            return 0;
        }
        if (N >= 1) {
            dp[1] = 1;
//            return 1;
        }
        if (N >= 2) {
            for (int ni = 2; ni <= N; ni++) {
                dp[ni] = dp[ni - 1] + dp[ni - 2];
                cout << " dp[" << ni <<  "]: " << dp[ni] << endl;
            }
        }
        return dp[N];
    }
};


