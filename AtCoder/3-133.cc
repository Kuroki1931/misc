int main() {
    string S;
    cin >> S;
    int N = S.size();
    int res = 0;
    for (int i = 0, i < N; i++) {
        int cnt = 0;
        for (int j = 1, j < N; j++) {
            char s = S[j];
            if (s == 'A' || s == 'C' || s == 'G' || s == 'T') {
                cnt++;
            } else {
                break;
            }
        }
        res = max(res, cnt)
    }
    cout << res << endl;
    return 0;
}