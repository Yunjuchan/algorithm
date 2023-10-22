K, N = map(int, input().split())

numbers = []
lst = []
Max = 0
for _ in range(K) :
    x = int(input())
    numbers.append(x)
    if x > Max :
        Max = x
for i in numbers :
    lst.append(str(i))
for _ in range(N-K) :
    lst.append(str(Max))

lst.sort(key=lambda x: (x * 10)[:10], reverse=True)
answer = ''.join(lst)

if answer[0] == '0':
    print(0)
else:
    print(answer)
