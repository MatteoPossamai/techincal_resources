#include <iostream>

using namespace std;

void bubble_sort(int array[], int len){
    for(int i=0; i<len;i++){
        for(int j=i+1;j<len;j++){
            if(array[i]>array[j]){
                int temp = array[j];
                array[j] = array[i];
                array[i] = temp;
            }
        }
    }
}

void printarray(const int array[], int len){
    for ( int i=0; i<len;i++){
        cout << array[i] << " ";
    }
}

int main(){
    int len = 11;
    int array [len] = {10,9,8,7,6,5,4,3,2,1,0};

    bubble_sort(array, len);

    printarray(array, len);

    return 0;
}