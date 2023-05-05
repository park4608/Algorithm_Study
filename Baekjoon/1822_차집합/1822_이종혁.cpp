#include <bits/stdc++.h>
using namespace std;

vector<int> a, b, res;
int n, m, c;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> c;
        a.push_back(c);
    }
    
    for (int i = 0; i < m; i++) {
        cin >> c;
        b.push_back(c);
    }

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    for (int i = 0; i < a.size(); i++) {
        if (binary_search(b.begin(), b.end(), a[i])) continue;
        res.push_back(a[i]);
    }

    cout << res.size() << "\n";
    for (int i = 0; i < res.size(); i++)
        cout << res[i] << " ";

    return 0;
}
