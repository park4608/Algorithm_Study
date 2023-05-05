#include <bits/stdc++.h>
using namespace std;

int n, m, a[500001], card[500001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++)  
        cin >> a[i];
    
    cin >> m;

    for (int i = 0; i < m; i++)
        cin >> card[i];
    
    sort(a, a + n);

    for (int i = 0; i < m; i++)
        cout << binary_search(a, a + n, card[i]) << ' ';

    return 0;
}
