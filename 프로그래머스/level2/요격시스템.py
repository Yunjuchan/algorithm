## 정렬하는 문제
## 미사일의 종료거리를 오름차순으로 정렬하여 
## 그다음 미사일의 시작거리가 더 크면 그 미사일의 종료거리로 기준을 변경하여
## 미사일을 발사

def solution(targets):
    targets.sort(key=lambda x : (x[1], x[0]))

    N = len(targets)
    answer = 1
    tmp = targets[0][1] - 0.5
    for i in range(N) :
        if targets[i][0] > tmp :
            answer += 1
            tmp = targets[i][1] - 0.5
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))