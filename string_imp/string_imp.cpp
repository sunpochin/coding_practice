#include "string_imp.h"


string_imp::string_imp() {
}

        
// string_imp::string_imp(const string_imp& pcstring) {
//     pcString_ = pcstring;
// }

// string_imp::string_imp(char const* pcValue) {
string_imp::string_imp(char* pcValue) {
    // strncpy(str, func, 255)
    pcString_ = pcValue;
}


string_imp& string_imp::operator=(const string_imp &strInst) {
}

string_imp& string_imp::operator=(const char* &strInst) {
}

bool string_imp::operator==(const string_imp &strInst) {
    return false;
}

bool string_imp::operator!=(const string_imp &strInst) {
    return false;
}

string_imp& string_imp::operator+(const string_imp &strInst) {

}

// std::ostream& operator<<(std::ostream &iostream, const string_imp &string) {
//     return (iostream << string->pcString_);   
// }
// std::basic_ostream& operator<<(std::ostream &iostream, const string_imp &string) {
//     return (iostream << string.pcString_);   
// }

// std::ostream& operator<<(std::ostream& stream, const string_imp &string) {
//     return (stream << string.pcString_);
// }

std::ostream& operator<<(std::ostream& stream, const string_imp &string) {
    return (stream << string.pcString_);
}

// std::basic_ostream<char>& operator<<(const string_imp& string) {
//     return (pcString_);
// }


char* string_imp::c_str() {
    return pcString_;
}

