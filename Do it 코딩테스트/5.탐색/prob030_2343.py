N, M = map(int, input().split())
lst = list(map(int, input().split()))
start = max(lst)
end = sum(lst)
def binarysearch(start, end) : 
    while start <= end :
        total = 0
        cnt = 1
        mid = (start + end) // 2
        for i in range(N) :
            total += lst[i]
            if total > mid :
                cnt += 1
                total = lst[i]     # 그 이전값까지가 리스트에 들어가기 마지막 값을 넣어줘서 초기화 해야함
            
        if cnt <= M :
            result = mid
            end = mid - 1
        else : start = mid + 1
    return result
print(binarysearch(start,end))
