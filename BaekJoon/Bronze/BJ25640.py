import sys
input = sys.stdin.readline

mbti = input()
case = int(input())
n = list(input() for _ in range(case))

cnt = 0
for _ in n:
    if mbti == _:
        cnt += 1
print(cnt)