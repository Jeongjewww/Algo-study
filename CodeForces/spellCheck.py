# issue unsolved^^..

import sys
input = sys.stdin.readline

def spellCheck():
    n = int(input()); s = input()

    if n == 5:
        for i in s:
            if i not in slist:
                return 'NO'
            return 'YES'
    else: return 'NO'

t = int(input()); ans = []
slist = 'Timur'
for _ in range(t):
    ans.append(spellCheck())
for _ in ans:
    print(_)