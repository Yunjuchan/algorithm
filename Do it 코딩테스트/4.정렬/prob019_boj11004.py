N, K = map(int, input().split())
lst = list(map(int, input().split()))
# lst.sort()
# print(lst[K-1])

def quick_sort(start, end, k) :
    if start < end :
        pivot = partition(start, end)
        if pivot == k :
            return
        elif k < pivot :
            quick_sort(start, pivot-1, k)
        else :
            quick_sort(pivot+1, end, k)

    
def partition(start, end) :
    if start == end - 1 :
        if lst[start] > lst[end] :
            lst[start], lst[end] = lst[end], lst[start]
        return end
    mid = (start + end) // 2    # 초기값 설정
    lst[start], lst[mid] = lst[mid], lst[start]

    pivot = lst[start]
    left = start + 1
    right = end

    while left <= right :
        while pivot < lst[right] and right > 0 :
            right -= 1
        while pivot > lst[left] and left < len(lst) - 1 :
            left += 1
        if left <= right :
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        
        lst[start] = lst[right]
        lst[right] = pivot
        return right
quick_sort(0, N-1, K-1)
print(lst[K-1])