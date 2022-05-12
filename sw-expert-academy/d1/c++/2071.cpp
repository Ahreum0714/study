#include <iostream>
#include <cmath>

using namespace std;

int solve() {
    float sum = 0;
    for(int i=0; i<10; i++) {
        int n;
        cin >> n;
        sum += n; 
    }

    return round(sum/10);
}

int main() {
    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        int result = solve();
        cout << "#" << i << " " << result <<endl;
    }
    return 0;
}