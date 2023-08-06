import sys
input = sys.stdin.readline
word = input().strip()
cursor = len(word)
N = int(input())

for i in range(N) :
    x = input().split()
    if x[0] == 'L' and cursor > 0 :
        cursor -= 1
    elif x[0] == 'D' and cursor < len(word) :
        cursor += 1
    elif x[0] == 'B' and cursor > 0 :
        word = word[:cursor-1] + word[cursor:]
        cursor -= 1
    elif x[0] == 'P' :
        word = word[:cursor] + x[1] + word[cursor:]
        cursor += 1
    else :
        pass
print(word)
