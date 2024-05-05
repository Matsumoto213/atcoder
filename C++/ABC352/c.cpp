#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;
    vector<int>A(N), B(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
    }

    int max_ = 0;
    for (int i = 0; i < N; i++) {
        max_ = max(max_, B[i] - A[i]);
    }

    long long ans = max_;
    for (int i = 0; i < N; i++) {
        ans += A[i];
    }
    cout << ans << endl;
}