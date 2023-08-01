st = input().replace(' ','')
idx1 = 1
idx2 = 2
result = None 
while idx1 < len(st) - 1 :
    st1 = st[:idx1] 
    st2 = st[idx1:idx2]
    st3 = st[idx2:]
    tmp = st1[::-1] + st2[::-1] + st3[::-1]
    if result == None   :
        result = tmp
    elif tmp < result :
        result = tmp
    # print(f'idx1:{idx1}, idx2:{idx2}, tmp:{tmp}')

    if idx2 >= len(st) - 1 :
        idx1 += 1
        idx2 = idx1 + 1
    else :
        idx2 += 1
print(result)

# 초기값을 st로 두었더니 계속 실패하였음
# st가 바꾸지 않았을때 가장 사전에서 빠른 단어일 때도 있기 때문이었음