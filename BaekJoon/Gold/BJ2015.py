# 시간 초과 에러, 미해결 --

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(len(num)):
    if k-num[i] in num:
        cnt += 1
print(cnt//2)