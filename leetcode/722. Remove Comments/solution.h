class Solution {
public:
    vector<string> removeComments(vector<string>& source) {
        
        vector<string> vans;
        bool binblock = false;
        string sline = "";
        for (auto it: source) {
            std::cout << "it: " << it << std::endl;
            for (int ni = 0; ni < it.size();) {
                if (!binblock) {
                    // the cursor currently not in a comment block.
                    // Traverse every character of this line.
                    if (ni <= it.size() - 1) {
                        string mk = it.substr(ni, 2);
                        if ("/*" == mk) {
                            binblock = true;
                            ni = ni + 2;
                        } else if ("//" == mk) {
                            // next line.
                            break;
                        } else {
                            sline = sline + it[ni];
                            std::cout << "sline: " << sline << std::endl;
                            ni++;
                        }
                    }
                } else {
                    // the cursor currently IN a comment block.
                    if (ni <= it.size() - 1) {
                        string mk = it.substr(ni, 2);
                        if ("*/" == mk) {
                            binblock = false;
                            ni += 2;
                        } else {
                            // sline = sline + it.substr(ni, 1);
                            ni++;
                        }
                    } 
                }
            }
            if (sline.size() && !binblock) {
                vans.push_back(sline);
                sline = "";
            }
        }
        return vans;
        
    }
};

