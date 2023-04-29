def solution(N_ropes, rope_weights):
    result = 0
    rope_weights.sort()

    for i, rope_weight in enumerate(rope_weights):
        tmp_result = rope_weight * (N_ropes - i)

        if tmp_result > result:
            result = tmp_result

    return result


N_ropes = int(input())
rope_weights = []
for _ in range(N_ropes):
    rope_weights.append(int(input()))
print(solution(N_ropes, rope_weights))
