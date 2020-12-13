#include <vector>
using std::vector;
#include <unordered_map>
using std::unordered_map;

// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         std::unordered_map<int, int> record;
//         for (int i = 0; i != nums.size(); ++i) {
//             auto found = record.find(nums[i]);
//             if (found != record.end())
//                 return {found->second, i};
//             record.emplace(target - nums[i], i);
//         }
//         return {-1, -1};
//     }
// };


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int ni = 0;
        int nj = 0;
        std::map<int, int> theMap;
        for (int iter = 0; iter < nums.size(); iter++) {
            theMap[nums[iter]] = iter;
                ni = theMap[nums[iter]];
                std::cout << "ni : " << ni << ", nums[iter] " << nums[iter] << std::endl;
        }
        
        vector<int> vecsolu;
        for (int iter = 0; iter < nums.size(); iter++) {
            int compen = target - nums[iter];
            std::cout << "compen : " << compen << std::endl;
            auto it = theMap.find(compen) ;
            if (it != theMap.end() ) {
                ni = it->second;
                std::cout << "ni : " << ni << std::endl;
                std::cout << "iter : " << iter << std::endl;
                
                if (ni == iter) {
                    continue;
                } else {
                    vecsolu.push_back(iter);
                    vecsolu.push_back(ni);
                    return vecsolu;
                    
                }
            }
        }

        return vecsolu;
        
        
        
    }
};