#include <iostream>
#include <cctype>

using namespace std;

int compute_letter_value(int n, int & res){
    char l;
    if ( n == 0){
        return 0;
    }else{
        cout << "Letter:" << endl;
        cout << res << endl;
        cin >> l;
        if (islower(l)){
            res += 5;
            return compute_letter_value(n-1, res);
        }else{
            res += 10;
            return compute_letter_value(n-1, res);
        }
    }
    
}

int main(){
    int n, res;
    cout << "Choose a number:" << endl;
    cin >> n;
    cout << "Insert " << n << " letters, and we will compute the total value" << endl;
    res  = compute_letter_value(n, res);

    cout << "The result is: " << res << endl;
    return 0;
}