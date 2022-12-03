#include <bits/stdc++.h>
using namespace std;

long long N, M, A[109][109];

int main() {
    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> A[i][j];
        }
    }

    long long ans = 0;
    for (int i = 1; i <= M; j++) {
        for (int j = i + 1; j <= M; j++) {
            long long cnt = 0;
            for (int k = 1; k <= N, k++) {
                cnt += max(A[k][i], A[k][j]);
                ans = max(ans, cnt);
            }
        }
    }
    cout << ans << endl;
    return 0;
}