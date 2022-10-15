# 에러잡기

import sys
input = sys.stdin.readline

word = input().lower()  # xxa
spell = list(set(word)) # spell=[x, a]

spl = []
for _ in spell:
    cnt = word.count(_)    # x:2, a:1
    spl.append(cnt) # spl=[2, 1]

if spl.count(max(spl)) > 1:     print("?")
else:   print(spell[(spl.index(max(spl)))].upper()) # X