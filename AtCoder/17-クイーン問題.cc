#include <bits/stdc++.h>
using namespace std;

bool is_feasible(const vector<part<int, int>> &constraint, const vector<int> &choice) {
    for (auto pr : constraint) {
        int r = pr.first;
        int c = pr.second;
        if (choice.at(r) != c) {return false}
    }
    for (int i = 0; i < 8; i++) {
        for (int j = i + 1; j < 8, j++) {
            int dx = j - i;
            int dy = choice.at(j) - choice.at(i);
            if (dx == dy || dx == -dy) {return false;}
        }
    }
    return true
}

int main() {
    int k;
    cin >> k;
    vector<pair<int, int>> constraint(k);
    int r, c:
    for (int i = 0; i < k; i++) {
        cin >> r >> c;
        contraint.at(i) = {r, c};
    }
    vector<int> choice(8);
    for (int i = 0; i < 8; i++) {
        choice.at(i) = i;
    }
    do {
        if (is_feasible(constraint, choice)) {
            break;
        } while (next_permutation(choice.begin(), choice.end()));
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8, j++) {
                if (choice.at(i) == j) {
                    cout << "Q";
                } else {
                    cout << ".";
                }
            }
        }
        cout << endl;
    } 
}