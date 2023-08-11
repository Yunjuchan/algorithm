N = int(input())
arr = [[i*j for j in range(1,N+1)] for i in range(1,N+1)]
K = int(input())
x = 1
while True :
    if 2*K <= x*(x+1) :
        res = K - (x*(x-1))//2
        break
    x += 1

if x > N :
    x = 2*N-x
else :
    pass
print(x)
print(res)
lst = [(N-x+i)*((N-x)+((x+1)-i)) for i in range(1,x+1)]
print(lst)
