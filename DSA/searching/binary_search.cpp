#include <iostream>

using namespace std;

int binary_search(int array[], int length, int element){
    int l = 0, h = length - 1, mid;

    if (array[l] == element){
        return l;
    }else if(array[h] == element){
        return h;
    }else{
        while (l <= h){
            mid = int((h + l) / 2);

            if (array[mid] == element){
                return mid;
            }else if(array[mid] < element){
                l = mid + 1;
            }else{
                h = mid - 1;
            }
        }
        return -1;
    }
  
}

int binarySearch(int A[], int low, int high, int x)
{
    if (low > high) {
        return -1;
    }
    int mid = (low + high) / 2;
    if (x == A[mid]) {
        return mid;
    }
    else if (x < A[mid]) {
        return binarySearch(A, low,  mid - 1, x);
    }
    else {
        return binarySearch(A, mid + 1,  high, x);
    }
}

int main(){
    int array[10] = {1,2,3,4,5,6,7,8,9,10};

    cout << binary_search(array, 10, 4) << endl;
    cout << binary_search(array, 10, 10) << endl;
    cout << binary_search(array, 10, 0) << endl;
    cout << binary_search(array, 10, 55) << endl;
    cout << binary_search(array, 10, 2) << endl;

    cout << binarySearch(array, 0,10, 4) << endl;
    cout << binarySearch(array, 0,10, 10) << endl;
    cout << binarySearch(array, 0,10, 0) << endl;
    cout << binarySearch(array, 0,10, 55) << endl;
    cout << binarySearch(array, 0,10, 2) << endl;
}