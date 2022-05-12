#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    int arr[n];
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    int smallest = arr[0];
    int largest = arr[0];
    for (int i=1; i<n; i++) {
        smallest = min(smallest, arr[i]);
        largest = max(largest, arr[i]);
    }
    cout << smallest << " " << largest <<endl;
    return 0;
}