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



# ## 내풀이도 실패
# N = int(input())
# K = int(input())
# x = 1
# flag = 0
# while True :
#     if K > N :
#         K = N**2 - K
#         flag = 1
#     if 2*K <= x*(x+1) :
#         res = K - (x*(x-1))//2
#         print(res)
#         break
    
#     x += 1
# print(x)
# if flag == 1 :
    
#     lst = [(N-x+i)*((N-x)+((x+1)-i)) for i in range(1,x+1)]
# else :
#     lst = [i*((x+1)-i) for i in range(1, x+1)]
# lst.sort()
# print(lst)
# # print(lst[res-1])
