import copy
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def mat_mul(mat1, mat2) :
    ret = [[0]*N for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            for k in range(N) :
                ret[i][j] += mat1[i][k]*mat2[k][j]
            ret[i][j] %= 1000
    return ret

def abc(level, arr) :
    if level == 1 :
        return arr
    
    mat = abc(level // 2, arr)
    return mat_mul(mat, mat) if level%2 ==0 else mat_mul(mat_mul(mat, mat),arr)
    
for a in abc(K, arr) :
    print(*a)