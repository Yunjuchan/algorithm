N = int(input())
lst1 = list(map(int, input().split()))
lst1.sort()
M = int(input())
lst2 = list(map(int, input().split()))
def binary_search(start, end, target) :
    while start <= end :
        mid = (start+end) // 2
        if target > lst1[mid] :
            start = mid + 1
        elif target < lst1[mid] :
            end = mid - 1
        else :
            return 1
    return 0
for i in range(M) :
    print(binary_search(0, N-1, lst2[i]))
