#include <iostream>

using namespace std;

int somma(int a, int b){
    if(b == 0){
        return a;
    }else if(a == 0){
        return b;
    }else{
        return 1 + somma(a, b-1);
    }
}

int prodotto(int a, int b){
    if (a == 0 || b == 0){
        return 0;
    }else if( a == 1){
        return b;
    }else if ( b == 1){
        return a;
    }else {
        return a + prodotto(a, b-1);
    }
}

int potenza(int a, int b){
    if (b == 0){
        return 1;
    }else if( b == 1){
        return a;
    }else{
        return a * potenza(a, b-1);
    }
}

int main(){
    int n1, n2;
    cout << "Insert the two numbers:";
    cin >> n1 >> n2;

    cout << "Somma di " << n1 << "+" << n2 << "=" << somma(n1, n2) << endl;
    cout << "Prodotto di " << n1 << "*" << n2 << "=" << prodotto(n1, n2) << endl;
    cout << "Potenza di " << n1 << " alla " << n2 << "=" << potenza(n1, n2) << endl;

    return 0;
}