/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
    // brute force solution
    const lp = 0
    const rp = 0
    let longestLen = 0
    for (lptr = 0; lptr <= s.length - 1; lptr += 1) {
        seenChar = {}
        curLeng = 0
        for (rptr = lptr; rptr <= s.length - 1; rptr += 1) {
            curChar = s[rptr]
//            console.log('charIdx: ', charIdx)
            charIdx = seenChar[curChar]
            console.log('curChar: ', curChar, ', charIdx: ', charIdx)
            if (!seenChar[curChar]) {
                seenChar[curChar] = true
                curLeng = rptr - lptr + 1
                console.log('rptr: ', rptr, ', lptr: ', lptr)
//                console.log('!seenChar[curChar]', 'longestLen: ', longestLen)
            } else {
                break
            }
        }
        longestLen = Math.max(longestLen, curLeng)
        console.log('curLeng: ', curLeng, ', longestLen: ', longestLen)
        
    }

    // while(rp <= s.length - 1) {
    //     curChar = s[rp]
    //     charIdx = seenChar[curChar]
    //     console.log('charIdx: ', charIdx)
    //     if (charIdx == -1) {

    //     }

    //     longestLen = rp - lp + 1

    //     rp += 1
    // }

    return longestLen

};

