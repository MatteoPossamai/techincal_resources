#include <iostream>

using namespace std;

void selection_sort(int array[], int len){
    for(int i=0;i<len;i++){
        int min = i;
        for(int j=i;j<len;j++){
            if (array[min]>array[j]){
                min = j;
            }
        }

        int temp = array[min];
        array[min] = array[i];
        array[i] = temp;
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

    selection_sort(array, len);

    printarray(array, len);

    return 0;
}