# def quick_sort(arr) :

arr = [9,7,5,3,1,2,4,6,8]
idx1 = 0
idx2 = len(arr) - 1
pivot = arr[idx2]
while idx1 < idx2 :
    if arr[idx2] < pivot < arr[idx1] :
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        idx1 += 1
        idx2 -= 1
    else :
        if arr[idx1] > pivot :
            idx1 += 1
        if arr[idx2] < pivot :
            idx2 -= 1
if arr[idx2] > pivot :
    left = arr[:idx2]
    # 피봇 집어넣으면
    right = arr[idx2+1:]
else :
    left = arr[:idx1]
    right = arr[idx1-1:]
