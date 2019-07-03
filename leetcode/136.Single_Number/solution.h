

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        std::set<int> theset;
        
        for (int niter = 0; niter < nums.size(); niter++) {
            int val = nums[niter];
            if (theset.find(val) == theset.end() ) {
                theset.insert(val);
            } else {
                theset.erase(val);
            }
        }
        
        int ans = *(theset.begin());
        return ans;
        
    }
};

