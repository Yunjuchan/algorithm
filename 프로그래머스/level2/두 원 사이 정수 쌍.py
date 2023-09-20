def solution(r1, r2):
    answer = (r2-r1+1)*4    # 축위의 점
    for i in range(1, r2) :
        x2 = r2**2 - i**2
        x1 = max(0, r1**2 - i**2-1)
        # 차이가 0보다 작으면 0으로 고정 작은 원에 닿기 전까지 
        answer += (int(x2**0.5) - int(x1**0.5)) * 4
        # 한쪽 사분면만 구해서 4 곱해서 덧셈
    return answer
r1, r2 = 5, 10
print(solution(r1, r2))