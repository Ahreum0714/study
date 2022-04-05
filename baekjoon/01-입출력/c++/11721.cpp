#include <iostream>
#include <string>

using namespace std;

int main() {
    string str;
    cin >> str;
    int n = str.length();
    int count = 0;

    for (int i = 0; i < n; i++) {
        printf("%c", str[i]);
        count++;
        if (count%10 == 0) 
            printf("\n");
    }
}