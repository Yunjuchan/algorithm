N = list(map(int, list(input())))
## merge sort 풀이
def merge_sort(arr) :
    if len(arr) >= 2 :
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        idx1 = idx2 = 0
        merged_list = []
        while True :
            if left[idx1] > right[idx2] :
                merged_list.append(left[idx1])
                idx1 += 1
            else :
                merged_list.append(right[idx2])
                idx2 += 1
            
            if idx1 == len(left) :
                merged_list += right[idx2:]
                return merged_list
            elif idx2 == len(right) :
                merged_list += left[idx1:]
                return merged_list
    else :
        return arr
print(*merge_sort(N))



