import sys
input = sys.stdin.readline

def od_ev():
    cnt = 0
    for _ in value:
        if _%2 == 0: cnt += 1
    if cnt == t//2: return 1
    else:   return 0

t = int(input())
value = list(map(int, input().split()))
print(od_ev())