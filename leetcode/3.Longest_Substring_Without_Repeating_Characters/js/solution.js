/**
 * @param {string} s
 * @return {number}
 */
 var lengthOfLongestSubstring = function(s) {
//     // ************************
//     // brute force solution
//     // ************************
//     let longestLen = 0
//     for (lptr = 0; lptr <= s.length - 1; lptr += 1) {
//         seenChar = {}
//         curLeng = 0
//         for (rptr = lptr; rptr <= s.length - 1; rptr += 1) {
//             curChar = s[rptr]
// //            console.log('charIdx: ', charIdx)
//             charExist = seenChar[curChar]
//             console.log('curChar: ', curChar, ', charExist: ', charExist)
//             if (!charExist) {
//                 seenChar[curChar] = true
//                 curLeng = rptr - lptr + 1
//                 console.log('rptr: ', rptr, ', lptr: ', lptr)
// //                console.log('!seenChar[curChar]', 'longestLen: ', longestLen)
//             } else {
//                 break
//             }
//         }
//         longestLen = Math.max(longestLen, curLeng)
//         console.log('curLeng: ', curLeng, ', longestLen: ', longestLen)
//     }
//     return longestLen

    // ************************
    // Optimal solution
    // ************************
    lptr = 0, rptr = 0
    seenChar = {}

    while(rptr <= s.length - 1) {
        curChar = s[rptr]
        charExist = seenChar[curChar]
        console.log('charExist: ', charExist)
        if (!charExist) {
            longestLen = rptr - lptr + 1
        }


        rp += 1
    }

    return longestLen

};

