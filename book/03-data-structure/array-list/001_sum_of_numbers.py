# 문제: 숫자의 합 구하기
# 유형: 배열과 리스트
# 핵심: 공백 없는 숫자 문자열을 한 글자씩 순회하며 합산

n = int(input())
numbers = input()

total = 0
for number in numbers:
    total += int(number)

print(total)