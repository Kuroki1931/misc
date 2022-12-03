#include <iostream>
#define rep(i,a,b) for(int i=a;i<b;i++)

int N, P[8], Q[8];
void main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> P[i];
    for (int i = 0; i < N; i++) cin >> Q[i];

    vector<int> v;
    for (int i = 0; i < N; i++) v.push_back(i + 1);
    int idx = 0, a = -1, b = -1;
    do {
        bool ok = true;
        for (i = 1; i < N; i++) if (v[i] != P[i]) ok = false;
        if (ok) a = idx;

        ok = true;
        for (int i = 1; i < N; i++) if (v[i] != Q[i]) ok = false;
        if (ok) b = idx;
        
        idx ++;
    } while (next_permutation(all(V)));

    int ans = abs(a - b);
    cout << ans << endl;
}