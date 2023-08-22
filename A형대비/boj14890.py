N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
def is_road_r(i) :
    flag = 0
    cnt = 0
    for j in range(N-1) :
        if abs(arr[i][j] - arr[i][j+1]) > 1 : 
            return 0
        
        if flag == 1 :
            if arr[i][j] == arr[i][j+1] :
                cnt += 1
                if cnt == L-1 :
                    flag = 0
                    cnt = -1
                continue
            else :
                return 0            
        
        if arr[i][j] - arr[i][j+1] == 1 :
            if L == 1 :
                flag = -1
                continue
            if flag != 0 :
                return 0
            cnt = 0
            flag = 1

        elif arr[i][j] - arr[i][j+1] == -1 :
            if flag == -1 :
                return 0
            if flag != 0 :
                return 0
            elif cnt < L-1 :
                return 0
            cnt = 0

        elif arr[i][j] == arr[i][j+1] :
            cnt += 1
            flag = 0

    if flag != 1 :
        return 1
    else :
        return 0

def is_road_c(i) :
    flag = 0
    cnt = 0
    for j in range(N-1) :
        if abs(arr[j][i] - arr[j+1][i]) > 1 :
            return 0
        
        if flag == 1 :
            if arr[j][i] == arr[j+1][i] :
                cnt += 1
                if cnt == L-1 :
                    flag = 0
                    cnt = -1
                continue
            else :
                return 0           
        
        if arr[j][i] - arr[j+1][i] == 1 :
            if L == 1 :
                flag = -1
                continue
            if flag != 0 :
                return 0
            cnt = 0
            flag = 1

        elif arr[j][i] - arr[j+1][i] == -1 :
            if flag == -1 :
                return 0
            if flag != 0 :
                return 0
            elif cnt < L-1 :
                return 0
            cnt = 0
            

        elif arr[j][i] == arr[j+1][i] :
            cnt += 1
            flag = 0

    if flag != 1 :
        return 1
    else :
        return 0




ret = 0
for i in range(N) :
    # print(is_road_r(i))
    # print()
    # print(is_road_c(i))

    ret += is_road_r(i) + is_road_c(i)
print(ret)