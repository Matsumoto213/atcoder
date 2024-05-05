#include <bits/stdc++.h>
using namespace std;

int main(){
    int N,X,Y,Z;
    cin >> N >> X >> Y >> Z;

    int max_ = max(X,Y);
    int min_ = min(X,Y);
    
    if (min_ <= Z && Z <= max_){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}