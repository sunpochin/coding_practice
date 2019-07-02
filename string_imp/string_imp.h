
class string_imp {
    private:
        char* pcString_;
    public:
        string_imp(void);
        string_imp(const string_imp&);
        // string_imp(char const* pcValue);
        string_imp(char* pcValue);

        string_imp& operator=(const string_imp &strInst);
        string_imp& operator+(const string_imp &strInst);

};

