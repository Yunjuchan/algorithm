## 문제가 개떡같아서 정리
## N개의 물병에는 1리터의 물이 들어있음
## 한번에 최대 K개의 물병의 상태를 변화시킬 수 있음
## 물이 차있는 물병을 K개 이하로 만들고 싶음
## 같은 물이 차있는 물병 두개를 선택
## 한쪽의 물을 비워줌 즉, 하나는 0 하나는 두배가 된다
## 다 완성시키지 못할 경우 물병을 새로 구매
## 즉 이건 2의 거듭제곱문제일 확률이 높음

N, K = map(int, input().split())
x = len(str(bin(N))[2:])
num = N
while num <= 2**x :     
    cnt = bin(num).count('1')

    if cnt <= K :
        print(num - N)
        break

    num += 1
else :
    print(-1)