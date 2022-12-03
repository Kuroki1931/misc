///値渡し
#include <iostream>

void twice(int a){
    std::cout << a << std::endl;
    a *= 2;
    std::cout << a << std::endl;
}

int main() {
    int v = 16;
    std::cout << v << std::endl;
    twice(v);
    std::cout << v << std::endl;
}

///ポインタ渡し
#include <iostream>
void twice(int* a) {
    std::cout << *a << std::endl;
}

int main() {
    int v = 16;
    std::cout << v << std::endl;
    twice(&v);
    std::cout << v << std::endl;
}

//ポインタ渡しnullチェック
#include <iostream>
bool twice(int& a) {
    if (a == nullptr) {
        std::cout << "null" << std::endl;
        return true;
    }
    std::cout << *a << std::endl;
    return false;
}

int main() {
    twice(nullptr);
    int v = 16;
    std::cout << v << std:endl;
    twice(&v);
    std::cout << v << std::endl;
}

//参照渡し
#include <iostream>
void twice(int* a) {
    std::cout << a << std:endl;
    a *= 2;
    std::cout << a << std::endl;
}

int main() {
    int v = 16;
    std::cout << v << std:endl;
    twice(v);
    std::cout << v << std::endl;
}

//オーバーロード
void twice(int& a) {
    std::cout << "call by reference." << std::endl;
    std::cout << a << std::endl;
    a *= 2;
    std::cout << a << std:endl;
}

bool twice(int* a) {
    std::cout << "call by pointer." << std::endl;
    if(a == nullptr) {
        std::cout << "null" << std::endl;
        return true;
    }
    twice(*a);
    return false;
}

int main() {
    int*p = nullptr;
    twice(p);

    int v = 16;
    int& r = v;
    p = &v;

    std::cout << "twice(v);" << std:endl;
    std::cout << v << std::endl;
    twice(v);
    std::cout << v << std::endl;

    std::cout << "twice(r);" << std::endl;
    std::cout << v << std::endl;
    twice(r);
    std::cout << v << std:endl;

    std::cout << "twice(p);" << std::endl;
    std::cout << v << std::endl;
    twice(p);
    std::cout << v << std::endl;
}