#include <iostream>
#include <cmath>

using namespace std;

double min(double x1, double x2){
    if (x1 < x2){
        return x1;
    }else{
        return x2;
    }
}

int jump_search(int arr[], int x, int n)
{
    int step = sqrt(n);

    int prev = 0;
    while (arr[min(step, n)-1] < x)
    {
        prev = step;
        step += sqrt(n);
        if (prev >= n)
            return -1;
    }
 
    while (arr[prev] < x){
        prev++;
        if (prev == min(step, n))
            return -1;
    }

    if (arr[prev] == x)
        return prev;
    return -1;
}

int main(){
    int array[10] = {1,2,3,4,5,6,7,8,9,10};

    cout << jump_search(array, 10, 4) << endl;
    cout << jump_search(array, 10, 10) << endl;
    cout << jump_search(array, 10, 0) << endl;
    cout << jump_search(array, 10, 55) << endl;
    cout << jump_search(array, 10, 2) << endl;
}