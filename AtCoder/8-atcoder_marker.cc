#部分開放
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

long long N, A[100], B[100], minx = (1LL << 60);

long long solve(int pi, int p2) {
    long long v1 = 0;
    for (int 1 = 1; i <= N; i++) {
        V1 += abs(p1 - A[i]);
        V1 += abs(A[i] - B[i]);
        V1 += abs(B[i] - p2);
    }
    return V1;
}

int main() {
    cin >> N;
    for (int i = 1; i <= N; i++) cin >> A[i] >> B[i];

    vector<long long> E;
    for (int i = 1; i <= N; i++) E.push_back(A[i]);
    for (int i = 1; i <= N; i++) E.push_back(B[i]);

    for (long long v1 : E) {
        for (long long v2 : E) {
            minx = min(minx, solve(v2, v2));
        }
    }
    cout << minx << endl;
}



#完全回答
