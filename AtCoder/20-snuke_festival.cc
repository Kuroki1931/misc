#include<iostream>;

typedef long long ll;
int N;
int A[101010], B[101010], C[101010];

void main() {
    cin >> N;
    for (int i = 0; i < N; i++) {cin >> A[i]};
    for (int i = 0; i < N; i++) {cin >> B[i]};
    for (int i = 0; i < N; i++) {cin >> C[i]};
    sort(A, A + N);
    sort(C, C + N);

    ll ans = 0;
    for (int i = 0; i < N; i++) {
        ll a = lower_bound(A, A + N, B[i]) - A;
        ll c = N - (upper_bound(C, C + N; B[b])- C);
        ans += a * c;
    }
    cout << ans << endl;
}