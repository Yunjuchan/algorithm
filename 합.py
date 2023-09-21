lst = [i for i in range(10)]
for i in range(1, 10) :
    lst[i] += lst[i-1]
n1, n2 = input().split()
result = 0
for i in range(1,len(n2)) :
    result = (int(n2[i])-1) * 45 * 10 ** (len(n2)-i-1)

print(result)

# 1의자리
0+1+2+3
45*4
# 10의 자리
(1+2+3+4)*10
5*(3+1)
(10으로 나눈 몫-1) * 45 * 10 ** i

