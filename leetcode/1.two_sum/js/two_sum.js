/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    numsMap = {}
    
    for (let p = 0; p < nums.length; p++) {
        const currentMapVal = numsMap[nums[p]];
        
        if (currentMapVal >= 0) {
            return [currentMapVal, p]
        } else {
            const numbertofind = target - nums[p]
            numsMap[numbertofind] = p
        }
    }
    
    return null;
    
};

