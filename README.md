# coding_practice
coding_practice



## Pattern: Binary Search:
  * Binary Search [here](leetcode)
  * Binary search: https://www.educative.io/courses/grokking-the-coding-interview/R8LzZQlj8lO <br>
    *  https://leetcode.com/problems/binary-search/ <br>
    * [my notes](leetcode/704.BinarySearch)
  * Ceiling of sorted array: https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7
    * https://www.geeksforgeeks.org/ceiling-in-a-sorted-array/
  * Find smallest letter greater than target: https://www.educative.io/courses/grokking-the-coding-interview/g2w6QPBA2Nk
    * https://leetcode.com/problems/find-smallest-letter-greater-than-target/submissions/


## Pattern: Finding Kth largest element in an array:
  * Top 'K' Numbers (easy): https://www.educative.io/courses/grokking-the-coding-interview/RM535yM9DW0
    * 215. Kth Largest Element in an Array: https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/


## Pattern: Merge k sorted lists:
  * https://www.educative.io/courses/grokking-the-coding-interview/Y5n0n3vAgYK
    * 23. Merge k Sorted Lists: 
      * leetcode 23. : https://leetcode.com/problems/merge-k-sorted-lists/
      * educative.io: https://www.educative.io/courses/grokking-the-coding-interview/Y5n0n3vAgYK

    * 378. Kth Smallest Element in a Sorted Matrix
      * leetcode 378. : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/submissions/
    * https://stackoverflow.com/questions/8753345/finding-kth-smallest-number-from-n-sorted-arrays

## Pattern: Palindromic Subsequence
  * 516. Longest Palindromic Subsequence
    * https://leetcode.com/problems/longest-palindromic-subsequence/
    * https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RMk1D1DY1PL


# Dynamic Programming
  * Tag: https://leetcode.com/tag/dynamic-programming/
  * Approach: https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.


## DP Pattern: DP: 0-1 Knapsack (0-1背包問題) 
  * 474. Ones and Zeroes: https://leetcode.com/problems/ones-and-zeroes/

## DP Pattern: Unbounded Knapsack
  * https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/gx763A3x9Pl
  * 

## DP Pattern 3: Fibonacci Numbers
### House Thief: 
  * https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2EOxJ0Nkp3
  * House Robber: https://leetcode.com/problems/house-robber/ 
  * House Robber 2: https://leetcode.com/problems/house-robber-ii/discuss/59921/9-lines-0ms-O(1)-Space-C%2B%2B-solution

    * https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation



## DP Pattern 3: Palindromic Subsequence
  * 516. Longest Palindromic Subsequence:  https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/RMk1D1DY1PL
    * https://leetcode.com/problems/longest-palindromic-subsequence/submissions/
  * 5. Longest Palindromic Substring: https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2yRjwxBY7A
  <pre>
    此题还可以用动态规划 Dynamic Programming 来解，根 Palindrome Partitioning II 的解法很类似，我们维护一个二维数组 dp，其中 dp[i][j] 表示字符串区间 [i, j] 是否为回文串，当 i = j 时，只有一个字符，肯定是回文串，如果 i = j + 1，说明是相邻字符，此时需要判断 s[i] 是否等于 s[j]，如果i和j不相邻，即 i - j >= 2 时，除了判断 s[i] 和 s[j] 相等之外，dp[i + 1][j - 1] 若为真，就是回文串，通过以上分析，可以写出递推式如下：
dp[i, j] = 1, if i == j
dp[i, j] = s[i] == s[j]
                                if j = i + 1
dp[i, j] = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1      
  </pre>

  * 647. Count of Palindromic Substrings
    


## DP Pattern 4: Palindromic Subsequence


