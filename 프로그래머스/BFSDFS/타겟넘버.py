def solution(numbers, target):
    answer = 0
    def dfs(start, numbers, target, Sum) :
        nonlocal answer
        if Sum < target :
            return 
        elif Sum == target :
            answer += 1
            return 
        for i in range(start, len(numbers)) :
            dfs(i+1, numbers, target, Sum-2*numbers[i])   
    Sum = sum(numbers)
    dfs(0,numbers, target, Sum)    

    return answer