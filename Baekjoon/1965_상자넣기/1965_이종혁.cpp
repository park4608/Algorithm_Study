﻿#include <bits/stdc++.h>
using namespace std;

int dp[1001];
int arr[1001];
int n, maxd = 1;

int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        dp[i] = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                dp[i] = max(dp[i], dp[j] + 1);
                maxd = max(maxd, dp[i]);
            }
        }
    }

    cout << maxd;
}