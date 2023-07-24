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


# while문 : 한번의 루틴은 1씩 증가한다. i번째 루틴은 i-1번 실행됨 (i > 1)
# N번째 분수의 분모와 분자의 합을 구하기 위해 i(i-1)/2 < N <= i(i+1)/2 를 만족해야함
# 그러한 코드를 구현하기 위해 while문을 설정하고 i값도 함께 저장

# 필자는 루틴의 마지막을 기준으로 문제를 풀었지만 루틴의 시작으로도 풀 수 있을 것이라 판단됨
# N번째 분수는 i번째 루틴에서 뒤에서 몇번째인지 알 수 있도록 두 수의 차이를 알 수 있는 cnt 변수를 만들었음
# 정리된 내용을 토대로 출력