#include <bits/stdc++.h>
using namespace std;

int main(void) {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string s;
	int res = 0;
	cin >> s;

	int len = s.length();


	for (int i = 0; i < len; i++) {
		if (s[i] != s[i - 1])
			res++;
	}

	if (res == 0)
		cout << 0;
	else
		cout << res / 2;
}