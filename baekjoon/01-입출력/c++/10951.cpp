#include <iostream>

using namespace std;

int main()
{
    int a, b;
    while(!(cin >> a >> b).eof()){
        cout << a+b << endl;
    }
    return 0;
}

// 좀 더 시간을  효율적으로 컨트롤할거라면
//while(scanf("%d %d", &a, &b) != EOF){
//	printf("%d\n", a + b);
//}
