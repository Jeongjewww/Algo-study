import sys
input = sys.stdin.readline

def bp(b, p):
    if b < 2: return 0
    else:
        if b >= 2*p: return p
        else: return b//2

b, p = map(int, input().split())
print(bp(b, p))