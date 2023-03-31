def solution(box_sizes):
    dp = []
    for (i, size) in enumerate(box_sizes):
        prev = 0
        for j in range(i):
            if box_sizes[j] < size and dp[j] > prev:
                prev = dp[j]
        dp.append(prev + 1)

    return max(dp)

_ = input()
print(solution(list(map(int, input().split()))))

# print(solution([1, 5, 2, 3, 7]))
# print(solution([1, 6, 2, 5, 7, 3, 5, 6]))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))