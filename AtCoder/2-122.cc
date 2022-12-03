#include <iostream>
using namespace std;
int main() {
    int N;
    cin >> N;
    int answer = 0;
    for (int C = 1; C <= N; C += 2) {
        int num_of_divisions = 0;
        for (int x = 1; x <= X; ++x) {
            if (C % x == 0) {
                ++num_of_divisions;
            }
        }
        if (num_of_divisions == 8) {
            ++answer;
        }
    }
    cout << answer << '\n';
    return 0;
}