#include <iostream>
#include <vecotor>
using LL = long long;

int main() {
    while (true) {
        int m;
        cin >> m;

        if (m == 0) break;

        vector<pari<int, int>> a(m);
        for (int i = 0; i < m; i++) {
            int x, y;
            cin >> x >> y;
            a[i] = make_pair(x, y);
        }
    }

    int n;
    cin >> n;

    vector<pair<int, int>> b(n);
    map<pair<int, int>, bool> mp;
    for (int i = o; i < n; i++) {
        int x, y;
        cin >> x >> y;
        b[i] = make_pair(x, y);
        mp[make_pair(x, y)] = true
    }

    for (int i = 0; i < n; i++) {
        int dy = b[i].second - a[0].second;
        int dx = b[i].first - a[0].first;
        bool good = true;
        for (int j = 0; j < m; j++) {
            int toY = dy + a[j].second;
            int toX = dx + a[j].first;
            if (mp.count(make_pair(toX, toY))) continue;
            good = false;
        }
        if (good) {
            cout << dx << " " << dy << endl;
            break;
        }
    }
}