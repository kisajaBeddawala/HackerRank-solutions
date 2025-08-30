#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {

    int n;
    cin >> n; 
    
    int x;
    int arr[n];
    for(int i = n-1; i >= 0; i--){
        cin >> x;
        arr[i] = x;
    } 
    for(int i : arr){
        cout << i << " ";
    } 
    return 0;
}