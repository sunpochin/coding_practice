
// https://leetcode.com/problems/partition-equal-subset-sum/


// class Solution {
//     public:
//       bool canPartition(const vector<int> &nums) {
//         int sum = 0;
//         for (int i = 0; i < nums.size(); i++) {
//           sum += nums[i];
//         }

//         // if 'sum' is a an odd number, we can't have two subsets with equal sum
//         if (sum % 2 != 0) {
//           return false;
//         }
          
//         vector<vector<int>> dp(nums.size(), vector<int>(sum / 2 + 1, -1));
//         return this->canPartitionRecursive(dp, nums, sum / 2, 0);
//       }

//     private:
//       bool canPartitionRecursive(vector<vector<int>>& dp, const vector<int> &nums, int sum, int currentIndex) {
//         // base check
//         if (sum == 0) {
//           return true;
//         }

//         if (nums.empty() || currentIndex >= nums.size()) {
//           return false;
//         }

//         // recursive call after choosing the number at the currentIndex
//         // if the number at currentIndex exceeds the sum, we shouldn't process this
//         // if we have not already processed a similar problem
//         if (dp[currentIndex][sum] == -1) {
//           // recursive call after choosing the number at the currentIndex
//           // if the number at currentIndex exceeds the sum, we shouldn't process this
//           if (nums[currentIndex] <= sum) {
//             if (canPartitionRecursive(dp, nums, sum - nums[currentIndex], currentIndex + 1)) {
//               dp[currentIndex][sum] = 1;
//               return true;
//             }
//           }

//           // recursive call after excluding the number at the currentIndex
//           dp[currentIndex][sum] = canPartitionRecursive(dp, nums, sum, currentIndex + 1) ? 1 : 0;
//         }

//         // recursive call after excluding the number at the currentIndex
//         return dp[currentIndex][sum] == 1 ? true : false;
//       }
// };




class Solution {
public:
  bool canPartition(const vector<int> &num) {
    int n = num.size();
    // find the total sum
    int sum = 0;
    for (int i = 0; i < n; i++) {
      sum += num[i];
    }

    // if 'sum' is a an odd number, we can't have two subsets with same total
    if (sum % 2 != 0) {
      return false;
    }

    // we are trying to find a subset of given numbers that has a total sum of ‘sum/2’.
    sum /= 2;

    vector<vector<bool>> dp(n, vector<bool>(sum + 1));

    // populate the sum=0 columns, as we can always for '0' sum with an empty set
    for (int i = 0; i < n; i++) {
      dp[i][0] = true;
    }

    // with only one number, we can form a subset only when the required sum is
    // equal to its value
    for (int s = 1; s <= sum; s++) {
      dp[0][s] = (num[0] == s ? true : false);
    }

    // process all subsets for all sums
    for (int i = 1; i < n; i++) {
      for (int s = 1; s <= sum; s++) {
        // if we can get the sum 's' without the number at index 'i'
        if (dp[i - 1][s]) {
          dp[i][s] = dp[i - 1][s];
        } else if (s >= num[i]) { // else if we can find a subset to get the remaining sum
          dp[i][s] = dp[i - 1][s - num[i]];
        }
      }
    }

    // the bottom-right corner will have our answer.
    return dp[n - 1][sum];
  }
};






