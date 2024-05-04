#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    cin >> N;

    vector<int> vec(N);
    int total = 0;
    for(int i = 0; i < N; i++){
        cin >> vec.at(i);
        total += vec.at(i);
    }

    int average = total / N;
    for(int i = 0; i < N; i++){
        cout << abs(average - vec.at(i)) << endl;
    }
}