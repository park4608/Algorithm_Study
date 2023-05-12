# [횟수, [결과]] 형태 페이로드
# 해싱으로 속도 최적화
# 2 일 때는 별도로 처리

from collections import deque


def solution(n_length, current_state, result_state):
    if current_state == result_state:
        return 0

    calculated = {current_state: False, result_state: True}
    queue = deque([[0, current_state]])

    while queue:
        node = queue.popleft()

        for i in range(n_length):
            next_state = (node[1][:max(0, i - 1)] + (('0' if node[1][i - 1] == '1' else '1') if i != 0 else '')) + \
                         ('0' if node[1][i] == '1' else '1') + \
                         ((('0' if node[1][i + 1] == '1' else '1') if i != n_length - 1 else '') + node[1][min(i + 2, n_length):])

            if calculated.get(next_state) is None:
                if next_state == result_state:
                    return node[0] + 1

                calculated[next_state] = False
                queue.append([node[0] + 1, next_state])
            elif calculated.get(next_state):
                return node[0] + 1
    return -1


N_length = int(input())
current_state = input()
result_state = input()
print(solution(N_length, current_state, result_state))


# print(solution(2, '00', '11'))
# print(solution(3, '000', '010'))
# print(solution(2, '11', '00'))
# print(solution(3, '000', '101'))
# print(solution(3, '000', '010'))
# print(solution(4, '0000', '0100'))
# print(solution(5, '00000', '01000'))
