import copy
N = int(input())
m = 0
lst = []
while N :
    m += 1
    lst.append(N%2)
    N //= 2
mat_list = []
mat = [[1,1],[1,0]]

for i in range(m) :
    mat_list.append(copy.deepcopy(mat))
    new_mat = [[0,0], [0,0]]
    for i in range(2) :
        for j in range(2) :
            for k in range(2) :
                new_mat[i][j] += mat[i][k] * mat[k][j]
                new_mat[i][j] %= 1000000007
    mat = copy.deepcopy(new_mat)

result = [[1,0],
          [0,1]]
for idx in range(m) :
    if lst[idx] == 1 :
        new_result = [[0,0], [0,0]]
        for i in range(2) :
            for j in range(2) :
                for k in range(2) :                
                    new_result[i][j] += result[i][k] * mat_list[idx][k][j]
                    new_result[i][j] %= 1000000007
        result = copy.deepcopy(new_result)   
print(result[0][1])             

    