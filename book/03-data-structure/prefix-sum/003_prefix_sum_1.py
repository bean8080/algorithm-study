# 문제: 구간 합 구하기 1
# 유형: 구간합
# 핵심: 누적합 배열을 미리 만들어 i부터 j까지의 합을 O(1)로 구한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]

total = 0

for number in numbers:
    total += number
    prefix_sum.append(total)

for _ in range(m):
    i, j = map(int, input().split())

    result = prefix_sum[j] - prefix_sum[i - 1]

    print(result)