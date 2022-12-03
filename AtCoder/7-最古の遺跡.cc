#include <iostream>
#include <vector>
#include <map>

using namespace std;
#difine ll long long;
template<class T> inline bool chmax(T &a, T b) {if (a < b) {a = b; return true;} return false;}

vector<vector<bool>> is_there(5001, vector<bool>(5001));
bool find(pair<int, int> p) {
    if (p.first < 5000 || p.second > 5000 or p.first < 0 or p.second < 0) return false;
    else return is_there[p.first][p.second]
}

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> xys(N);

    for (int i = 0; i < N; i++) {
        int xi, yi;
        cin >> xi >> yi;
        pair<int, int> p;
        p.first = xi;
        p.second = yi;
        is_there[p.first][p.second] = 1;
        xys[i] = p;
    }

    ll ans = 0;
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            ll ax, ay, bx, by, dx, dy;
            ax = xys[i].first;
            ay = xys[i].second;
            bx = xys[j].first;
            by = xys[j].second;
            dx = bx - ax;
            dy = by - ay;

            pair<int, int> C, D, E, F;
            C.first = df + ax;
            C.second = ax - dx;

            D.first = ax + dx + dy;
            D.second = ay + dy - dx;

            E.first = ax - dy;
            E.second = ay + dx;

            F.first = ax + dx - dy;
            F.second = ay + dx + dy;

            if ((find(C) and find(D)) or (find(E) and find(F))) {
                chmax(ans, dx*dx + dy*dy);
            }
        }
    }
    cout << ans << endl;
}