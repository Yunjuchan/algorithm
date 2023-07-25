## 17427을 이용하려고 했지만 확장이 되지 않았음.
# import sys
# input = sys.stdin.readline
# T = int(input())
# for t in range(T) :
#     N = int(input())
#     total = 0
#     for i in range(1, N+1) :
#         total += (N // i) * i
#     print(total)


# 약수의 개념으로 들어가서 약수일때만 호출될 수 있도록 출력하여 nlogn으로

import sys
input = sys.stdin.readline
n = 1000000
div_arr = [1] * (n + 1)
accu_arr = [0] * (n + 1)
accu_arr[1] = 1
for i in range(2, n+1) :    # 약수 : C
    for j in range(1, (n // i) + 1) :   # 배수 : B
        div_arr[i * j] += i     # i * j 가 원래 수 : A
    accu_arr[i] = accu_arr[i-1] + div_arr[i]
T = int(input())
for t in range(T) :
    num = int(input())
    print(accu_arr[num])

## python3은 컴파일 속도가 매우 느림 -> pypy3가 컴파일 속도가 빨라서
## 대체하였더니 잘 나왔음

## 약수문제에서 힘들었던 부분 : A에서 B와 C를 찾아내려고 했던게 시간복잡도를 향상시켰음
## 곱셈이나 두 개를 합쳐서 큰 값을 만들어낼때 불필요한 호출수 를 줄일 수 있음
