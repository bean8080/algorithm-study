# 문제: 구간 합 구하기 2
# 유형: 2차원 구간합
# 핵심: 2차원 누적합 배열을 만들어 직사각형 구간의 합을 O(1)로 구한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

table = [[0] * (n + 1)]

for _ in range(n):
    row = [0] + list(map(int, input().split()))
    table.append(row)

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        prefix_sum[x][y] = (
                prefix_sum[x - 1][y]
                + prefix_sum[x][y - 1]
                - prefix_sum[x - 1][y - 1]
                + table[x][y]
        )

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = (
            prefix_sum[x2][y2]
            - prefix_sum[x1 - 1][y2]
            - prefix_sum[x2][y1 - 1]
            + prefix_sum[x1 - 1][y1 - 1]
    )

    print(result)