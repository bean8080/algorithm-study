# 문제: 평균 구하기
# 유형: 배열과 리스트
# 핵심: 최댓값을 기준으로 점수를 보정한 뒤 평균을 구한다.

n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

total = 0

for score in scores:
    total += score / max_score * 100

print(total / n)