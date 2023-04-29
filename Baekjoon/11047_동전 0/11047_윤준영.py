def solution(K_goal, coin_values):
    result, index = 0, len(coin_values) - 1
    while index >= 0:
        if K_goal >= coin_values[index]:
            K_goal -= coin_values[index]
            result += 1
        else:
            index -= 1

    return result

N, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
print(solution(K, A))