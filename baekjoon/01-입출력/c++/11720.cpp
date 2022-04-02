#include <iostream>
#include <string>

using namespace std;

int main() {
    int n, sum = 0;
    string numbers;

    cin >> n;
    cin >> numbers;
    for (int i = 0; i < n; i++) {
        int int_value = numbers[i] - '0';
        sum += int_value;
    }
    cout << sum <<endl;
}