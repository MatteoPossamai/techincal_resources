#include <iostream>

using namespace std;

int mcdCalculator(int a, int b){
    if (b==0){
        return a;
    }else{
        return mcdCalculator(b, a%b);
    }
}

int main(){
    int a, b, mcd;
    cin >> a >> b;

    mcd = mcdCalculator(a, b);
    cout << mcd << endl;

    return 0;
}