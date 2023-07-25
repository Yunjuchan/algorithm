st = input()
result = st
idx1 = 0
idx2 = 1
while idx1 < len(st) - 2 :
    tmp = st[idx1::-1] + st[idx2:idx1:-1] +st[:idx2:-1]
    if tmp < result :
        result = tmp
    print(f'idx1:{idx1}, idx2:{idx2}, tmp:{tmp}')

    if idx2 >= len(st) - 2 :
        idx1 += 1
        idx2 = idx1 + 1
    else :
        idx2 += 1
print(result)