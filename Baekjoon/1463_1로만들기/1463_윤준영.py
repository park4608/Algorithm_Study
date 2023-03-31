import math

def solution(n):
    dp = [0, 0, 1, 1]

    for i in range(4, n + 1):
        dp.append(min(dp[i // 2] + 1 if i % 2 == 0 else math.inf,
                      dp[i // 3] + 1 if i % 3 == 0 else math.inf,
                      dp[i - 1] + 1))

    return dp[n]

print(solution(int(input())))