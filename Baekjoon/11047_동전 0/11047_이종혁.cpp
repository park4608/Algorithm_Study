#include <iostream>
using namespace std;

int n, k, arr[11];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int res = 0;

    cin >> n >> k;

    for (int i = 0; i < n; i++) cin >> arr[i];

    for (int i = n - 1; i >= 0; i--) {
        res += k / arr[i];
        k %= arr[i];
    }

    cout << res;

    return 0;
}
