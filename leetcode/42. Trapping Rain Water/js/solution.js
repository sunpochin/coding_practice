/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let totalwater = 0;
    for (p = 0; p < height.length; p++) {
        let leftp = p - 1, rightp = p, leftmax = 0, rightmax = 0;
        while(leftp >= 0) {
            leftmax = Math.max(height[leftp], leftmax)
//            console.log('leftmax: ', leftmax)
            leftp--
        }
        while(rightp < height.length) {
            rightmax = Math.max(height[rightp], rightmax)
//            console.log('rightmax: ', rightmax)
            rightp++
        }
        const curwater = Math.min(leftmax, rightmax) - height[p]
        if (curwater > 0) {
            totalwater += curwater
        }
        console.log('p: ', p, ', curwater: ', curwater, ', totalwater: ', totalwater)
        
    }
    
    return totalwater
    
};