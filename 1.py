from collections import deque
word = input()
num_a, num_b = 0, 0
for ch in word :
    if ch == 'a' :
        num_a += 1
    else : 
        num_b += 1

if num_a < num_b :
    target = 'a'
    word += word[:num_a]
    i, j = 0, num_a
    num_t = Min = num_a
else :
    target = 'b'
    word += word[:num_b]        
    i, j = 0, num_b
    num_t = Min = num_b
n = len(word)

while j <= n :
    tmp = num_t - word[i:j].count(target)
    if tmp < Min :
        Min = tmp
    i += 1
    j += 1
print(Min)
