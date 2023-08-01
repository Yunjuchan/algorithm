A, B, N = map(int, input().split())
i = 0   
result = None
# 소수 아래 N번째까지 구하기 위해 while문으로 반복 
while i <= N :
    result, tmp = divmod(A, B) 
    A = tmp * 10
    i += 1
print(result)

# 0번째 result는 몫이 나옴
# 1번째부터 소수가 나오므로
# N번째는 while문이 N+1번 반복 되어야함