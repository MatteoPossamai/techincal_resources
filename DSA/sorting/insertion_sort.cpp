#include <iostream>
using namespace std;

void insertion_sort(int array[], int len){
    for(int i=0;i<len;i++){
        int j = i;
        while(j > 0 && array[j-1] > array[j]){
            int temp = array[j];
            array[j] = array[j-1];
            array[j-1] = temp;
            j --;
        }
    }
}

void printarray(const int array[], int len){
    for ( int i=0; i<len;i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(){
    int len = 11;
    int array [len] = {10,9,8,7,6,5,4,3,2,1,0};

    insertion_sort(array, len);

    printarray(array, len);

    return 0;
}