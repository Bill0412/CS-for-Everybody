#include <iostream>

using namespace std;

// 1. overload version of add
int add1(int a, int b) {
    return a + b;
}

double add1(double a,double b) {
    return a + b;
}

// 2. C++ function template
// explicitly specify the type of arguments and return value
template<typename number> number add2(number a, number b) {
    return a + b;
}


int main()
{
    cout << add1(1, 2) << endl;
    cout << add1(2.2, 3.3) << endl;
    cout << add2(1, 2) << endl;
    cout << add2(2.2, 3.3) << endl;
}