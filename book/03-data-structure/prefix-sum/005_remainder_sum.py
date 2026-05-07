# 문제: 나머지 합 구하기
# 유형: 구간합
# 핵심: 누적합을 M으로 나눈 나머지가 같은 두 지점을 고르면 그 사이 구간합은 M으로 나누어떨어진다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

remainder_count = [0] * m

total = 0
answer = 0

for number in numbers:
    total += number

    remainder = total % m

    if remainder == 0:
        answer += 1

    answer += remainder_count[remainder]

    remainder_count[remainder] += 1

print(answer)