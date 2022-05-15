#include<iostream>
#include<vector>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
	cin>>T;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        int n, score, ans = 0;
        cin >> n;

        vector<int> v(101);

        for (int i = 0; i < 1000; i++) {
            cin >> score;
            v[score]++;
        }

        for (int i = 1; i < 101; i++) {
            if (v[i] >= v[ans])
                ans = i;
        }

        cout << "#" << n << " " << ans << endl;
	}
	return 0;
}