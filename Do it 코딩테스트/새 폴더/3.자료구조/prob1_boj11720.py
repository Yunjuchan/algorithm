# 풀이 숫자계산
N = int(input())
x = int(input())
result = 0
for i in range(N) :
    result += x % 10
    x = x // 10
print(result)

# 풀이 리스트
N = int(input())
a = list(input())
total = 0
for i in a :
    total += int(i)
print(total)