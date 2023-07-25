# ## N을 곱해서 푸는 방법 : 시간이 너무 오래걸림
# import sys
# input = sys.stdin.readline
# N = int(input())
# i = 1
# while True :
#     x = N * i
#     cnt = 0
#     while x > 0 :
#         if x % 10 == 1 :
#             x = x // 10
#             cnt += 1
#         else :
#             cnt = 0
#             i += 1
#             break
#     if cnt > 0 :
#         break
# print(cnt)


# ## 1을 한자리씩 늘려서 풀어가는 방법
import sys
input = sys.stdin.readline
while True :
    try :
        num = 1
        N = int(input())
        while True :
            if num % N == 0 :
                print(len(str(num)))
                break
            else :
                num = num * 10 + 1
    except :
        break

