
415. Add Strings
Easy

414

145

Favorite

Share
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.



*** The point is num1[i] - '0'  is an integer.

https://leetcode.com/problems/add-strings/discuss/90453/C%2B%2B_Accepted_13ms




class Solution {
public:
string addStrings(string num1, string num2) {
    int i = num1.size() - 1;
    int j = num2.size() - 1;
    int carry = 0;
    string res = "";
    while(i>=0 || j>=0 || carry){
        long sum = 0;
        if(i >= 0){sum += (num1[i] - '0');i--;}
        if(j >= 0){sum += (num2[j] - '0');j--;}
        sum += carry; 
        carry = sum / 10;
        sum = sum % 10;
        res =  res + to_string(sum);
    }
    reverse(res.begin(), res.end());
    return res;
}
};