#include <iostream>

using namespace std;

int main()
{
    int num, i;
    cin >> num;
    int a[num], b[num];
    for(i = 0; i<num; i++){
        cin >> a[i] >> b[i];
    }
    for (i = 0; i<num; i++)
    cout << a[i]+b[i] << endl;
    return 0;
}
