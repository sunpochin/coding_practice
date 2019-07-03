class Solution {
public:
    int countSegments(string s) {
        int segcnt = 0;
        for (int ni = 0; ni < s.size(); ni++) {
            if (s.at(ni) != ' ' && 0 == ni 
                || (s.at(ni) != ' ' && s.at(ni - 1) == ' ')
               ) {
                segcnt++;
            }
            
        }
        return segcnt;
    }
};


