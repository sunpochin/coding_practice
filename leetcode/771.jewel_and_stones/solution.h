#include <set>

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int ans = 0;
        set<char> setJ;
        set<char> setS;
        
        for (int ni = 0; ni < J.size(); ni++) {
//            cout << "J[ni] : " << J[ni] << std::endl;
            setJ.insert(J[ni]);
        }
        for (int ni = 0; ni < S.size(); ni++) {
            if (setJ.find(S[ni]) != setJ.end() ) {
                ans++;
            }
        }
        
        return ans;
        
    }
};
