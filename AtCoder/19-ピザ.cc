#include <bits/stdc++.h>
using namespace std;

int calc_dist<const vector<int> &d_vec, int k) {
    auto it = lower_bound(d_vec.begin(), d_vec.end(), k);
    if (*it == k){
        return 0
    }
    return min(k - *(it - 1), *it - k);  
}

int main() {
    int d, n, m;
    cin >> d >> n >> m;
    vector<int> d_vec(n + 1)
    d_vec.at(0) = 0;
    d_vec.at(n) = d;
    for (int i = 1; i < n; i++){
        cin >> d_vec.at(i);
    }
    vector<int> k_vec(m);
    for (int i = 0; i < m; i++) {
        cin >> k_vec.at(i);
    }
    sort(d_vec.begin(), d_vec.end());
    int sum_dist = 0;
    for (int i = 0; i < m, i++) {
        int dist = calc_dist(d_vec, k_vec.at(i));
        sum_dist += dist;
    }
    cout << sum_dist << endl;
}