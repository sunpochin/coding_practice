/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(heights) {
    let maxTemp = 0;
    for (let p1 = 0; p1 < heights.length; p1++) {
        for (let p2 = p1 + 1; p2 < heights.length; p2++) {
            const height = Math.min(heights[p1], heights[p2]);
            const width = p2 - p1;
            const area = height * width;
            maxTemp = Math.max(maxTemp, area)
        }
    }
    
    return maxTemp
};

