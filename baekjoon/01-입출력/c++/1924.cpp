#include <iostream>

using namespace std;

int main () {
    // 1  2  3  4  5  6  7  8  9 10  11  12
    // 31,28,31,30,31,30,31,31,30,31,30,31
    int x, y, k, total_days = 0;
    int days[] = {31,28,31,30,31,30,31,31,30,31,30,31};

    cin >> x >> y;

    // 전월까지의 일수 더하기
    for (int i=0; i<x-1; i++) {
        total_days += days[i];
    }
    // 당월의 일자 일수까지 더하기
    total_days += y;

    // 총 일수에서 7로 나누기
    // 나머지 1이면 월요일, 2이면 화요일, 3이면 수요일, 4이면 목요일, 5이면 금요일, 6이면 토요일, 0이면 일요일
    k = total_days % 7;
    switch (k)
    {
    case 0:
        cout << "SUN" <<endl;
        break;
    case 1:
        cout << "MON" <<endl;
        break;
    case 2:
        cout << "TUE" <<endl;
        break;
    case 3:
        cout << "WED" <<endl;
        break;
    case 4:
        cout << "THU" <<endl;
        break;
    case 5:
        cout << "FRI" <<endl;
        break;
    case 6:
        cout << "SAT" <<endl;
        break;
    default:
        break;
    }

    return 0;
}