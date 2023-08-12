# N = int(input())
# K = int(input())
# start = 1
# end = K
# ans = 0 
# while start <= end :
#     mid = (start + end) // 2
#     cnt = 0
#     for i in range(1, K+1) :
#         cnt += min(mid // i, N)

#     if K > cnt :
#         start = mid + 1
#     else :
#         ans = mid
#         end = mid - 1
# print(ans)

N = int(input())
K = int(input())
x = 1
while True :
    if 2*K <= x*(x+1) :
        res = K - (x*(x-1))//2
        print(res)
        break
    x += 1
print(x)
if x > N :
    x = 2*N-x
    lst = [(N-x+i)*((N-x)+((x+1)-i)) for i in range(1,x+1)]
else :
    lst = [i*((x+1)-i) for i in range(1, x+1)]
lst.sort()
print(lst)
# print(lst[res-1])
