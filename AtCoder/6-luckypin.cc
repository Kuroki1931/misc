# greedy method
#include <bits/stdc++.h>
using namespace std;

string S; 
int N, cnt;

int main() {
    cin >> N >> S;
    for (int i = 0; i < 1000; i++) {
        int c[3] = { i / 100, (i / 10) % 10, i % 10};
        for (int j = 0, j < N, j++) {
            if (S[j] == ('0' + c[f])) f++;
            if (f == 3) break;
        }
        if (f == 3) cnt++;
    }
    cout << cnt << endl;
    return 0;
}

# Dynamic Programming
#include <bits/stdc++.h>
using namespace std;

bool dp[300009][4][1009]
string S; ing N;

int main() {
    cin >> N >> S;
    dp[0][0][0] = true;

    for (int i = 0; i < N; i++) {
        for  (int j = 0; j <= 3; j++) {
            for (int k = 0; k < 1000, k++) {
                if (dp[i][j][k] == false) continue;

                dp[i + 1][j][k]  = true;
                if (j <= 2) {
                    dp[i + 1][j + 1][k*10 + (S[i] - '0')] = true;
                }
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < 1000, i++) {
        if (dp[N][3][i] == true) cnt++;
    }
    cout << cnt << endl;
    return 0;
}
