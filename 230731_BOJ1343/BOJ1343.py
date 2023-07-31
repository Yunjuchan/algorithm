X = input().split('.')
A = 'AAAA'
B = 'BB'
new_word = []
for i in X :
    tmp = ''
    if len(i) == 0 : 
        new_word.append(tmp)
        continue
    elif len(i) % 2 == 1 :
        print(-1)
        break
    elif len(i) % 4 == 0 :
        tmp += A * (len(i) // 4)
    elif len(i) % 2 == 0  :
        tmp += A * (len(i) // 4) + B
    new_word.append(tmp)
else :
    print('.'.join(new_word))