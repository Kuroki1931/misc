#include <bits/stdc++.h>
using namespace std;

bool contains(const vector<int> &S_vec, int t) {
    auto lb = lower_bound(S_vec.begin(), S_vec.end(), t);
    return (lb != S_vec.end()) && (*lb == t);
}

int main() {
    int n;
    cin >> n;
    vector<int> S_vec(n);
    for (int i = 0; i < n; i++) {
        cin >> S_vec.at(i);
    }
    int q;
    cin >> q;
    vector<int> T_vec(q);
    for (int i = 0; i < q; i++) {
        cin >> T_vec.at(i);
    }
    int cnt = 0;
    for (int i = 0; i < q; i++) {
        if (contains(S_vec, T_vec.at(i))) {
            cnt++;
        }
    }
    cout << cnt << endl;
}