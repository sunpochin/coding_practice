/**
 * @param {string} s
 * @return {boolean}
 */
 var validPalindrome = function(s) {
    let rstr = s.split("").reverse().join("");
    // console.log('reversed: ', rstr)

    if (rstr == s) {
        return true
    }

    for (let it = 0; it < s.length; it += 1) {
        if (s[it] != rstr[it]) {
            // check two strings if palindrome.
            // console.log('it: ', it, ', s[it]: ', s[it], ', rstr[it]:', rstr[it])
            snew = s.slice(0, it) + s.slice(it + 1, s.length)
            rnew = rstr.slice(0, it) + rstr.slice(it + 1, rstr.length)
            
            snewre = snew.split("").reverse().join("");
            rnewre = rnew.split("").reverse().join("");
            if (snew == snewre || rnew == rnewre) {
                return true
            } else {
                // console.log('snew: ', snew, ', rstr:', rstr, ', s:', s, ', rnew: ', rnew)
                return false
            }
        } else {
            continue
        }
    }
    return true
};

