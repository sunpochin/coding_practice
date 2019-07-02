
#include <iostream>


class string_imp {
    private:
    public:
        char* pcString_;
        string_imp(void);

        // string_imp(const string_imp& pcstring);
        // string_imp(char const* pcValue);
        string_imp(char* pcValue);
        string_imp& operator=(const string_imp &strInst);
        string_imp& operator=(const char* &strInst);
        string_imp& operator+(const string_imp &strInst);

        bool operator==(const string_imp &strInst);
        bool operator!=(const string_imp &strInst);

        // std::ostream& operator<<(std::ostream &iostream, const string_imp &string);
        // std::ostream& operator<<(std::ostream& stream, const string_imp& string);
        // std::ostream& operator<<(const string_imp& string);
        char* c_str();

};

std::ostream& operator<<(std::ostream& stream, const string_imp& string);


