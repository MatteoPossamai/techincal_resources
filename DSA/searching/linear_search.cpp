#include <iostream>

using namespace std;

int linear_search(int array[], int length, int element){
    int result = -1;
    for (int i = 0, found = 0; i< length && found == 0; i++){
        if (array[i] == element){
            result = i;
            found = 1;
        }
    }
    return result;
}

int main(){
    int array[10] = {1,2,3,4,5,6,7,8,9,10};

    cout << linear_search(array, 10, 4) << endl;
    cout << linear_search(array, 10, 10) << endl;
    cout << linear_search(array, 10, 0) << endl;
    cout << linear_search(array, 10, 55) << endl;
    cout << linear_search(array, 10, 2) << endl;
}