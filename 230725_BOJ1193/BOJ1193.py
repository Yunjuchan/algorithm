N = int(input())
total = 0
i = 1
while N > total : 
    total += i
    i += 1
cnt = total - N
if i % 2 == 1 :
    print(f'{i-1-cnt}/{1+cnt}')
else :
    print(f'{1+cnt}/{i-1-cnt}')