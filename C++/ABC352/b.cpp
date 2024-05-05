#include <bits/stdc++.h>
using namespace std;

int main(){
    string S, T;
    cin >> S >> T;

    int s_index = 0;
    
    // Sに入力されたものがTの最初から見て何文字目かを出力する
    for (int t_index = 0; t_index < T.size(); t_index++){
        if (T[t_index] == S[s_index]){
            cout << t_index + 1 << ' ';
            s_index += 1;
        }
    }
}