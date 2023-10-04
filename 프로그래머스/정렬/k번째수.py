def solution(array, commands):
    answer = []
    for s, e, idx in commands :
        tmp = array[s-1:e]
        tmp.sort()
        answer.append(tmp[idx-1])
    return answer