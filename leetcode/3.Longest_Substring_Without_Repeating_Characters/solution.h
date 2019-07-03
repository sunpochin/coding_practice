
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        set<char> theset;

        int ans = 0, i = 0, j = 0;
        const int nsize = s.size();
        while(i < nsize && j < nsize) {
            if (theset.find(s[j]) != theset.end() ) {
                theset.insert(s[j]);
                j++;
                ans = std::max(ans, j - i);
            } else {
                theset.erase(s[j]);
            }
        }
        
        return ans;
        
    }
};

