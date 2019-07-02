
#include "string_imp.h"
// #include <stdio.h>
#include <cassert>

int main() {
    std::cout << "main: " << std::endl;
    string_imp imp1 = "1";
    std::cout << "imp1: " << imp1 << std::endl;
    string_imp imp2 = "2";
    std::cout << "imp2: " << imp2 << std::endl;

    assert(imp1 != imp2);
    assert(imp1 == "1");
    assert(imp2 == "2");

    return 0;
}

