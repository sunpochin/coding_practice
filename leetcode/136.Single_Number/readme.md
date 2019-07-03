136. Single Number
Easy

2287

86

Favorite

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4





answer:

Solution
Approach 1: List operation
Algorithm

Iterate over all the elements in \text{nums}nums
If some number in \text{nums}nums is new to array, append it
If some number is already in the array, remove it

Complexity Analysis

Time complexity : O(n^2)O(n 
2
 ). We iterate through \text{nums}nums, taking O(n)O(n) time. We search the whole list to find whether there is duplicate number, taking O(n)O(n) time. Because search is in the for loop, so we have to multiply both time complexities which is O(n^2)O(n 
2
 ).

Space complexity : O(n)O(n). We need a list of size nn to contain elements in \text{nums}nums. 


Approach 2: Hash Table
Algorithm

We use hash table to avoid the O(n)O(n) time required for searching the elements.

Iterate through all elements in \text{nums}nums
Try if hash\_tablehash_table has the key for pop
If not, set up key/value pair
In the end, there is only one element in hash\_tablehash_table, so use popitem to get it

Complexity Analysis

Time complexity : O(n \cdot 1) = O(n)O(n⋅1)=O(n). Time complexity of for loop is O(n)O(n). Time complexity of hash table(dictionary in python) operation pop is O(1)O(1).

Space complexity : O(n)O(n). The space required by hash\_tablehash_table is equal to the number of elements in \text{nums}nums. 


Approach 3: Math
Concept

2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c)−(a+a+b+b+c)=c

