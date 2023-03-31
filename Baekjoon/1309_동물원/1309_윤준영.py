def solution(n):
    dp = [1, 3, 7, 17, 41]

    if n <= 4:
        return dp[n]

    for i in range(5, n + 1):
        dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)

    return dp[n]

print(solution(int(input())))