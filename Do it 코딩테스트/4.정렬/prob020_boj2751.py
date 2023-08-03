N = int(input())

lst = [int(input()) for _ in range(N)]
def merge_sort(lst) :
    if len(lst) == 1 :
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    i = j = 0
    merged_lst = []
    while True :
        if left[i] < right[j] :
            merged_lst.append(left[i])
            i += 1
        else :
            merged_lst.append(right[j])
            j += 1
        if i == len(left) :
            merged_lst += right[j:]
            return merged_lst
        elif j == len(right) :
            merged_lst += left[i:]
            return merged_lst
sorted_lst = merge_sort(lst)
for i in range(N) :
    print(sorted_lst[i])