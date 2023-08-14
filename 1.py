def abc(level) :
    global cnt, flag
    if path == word :
        flag = 1
        print(cnt)
        return
    for i in range(26) :
        path.append(i)
        abc(level+1)
        if flag == 1 :
            return
        path.pop()
    pass
N = int(input())

for _ in range(N) :
    path = []
    word = list(input())
    for i in range(len(word)) :
        word[i] = ord(word[i]) - ord('A')
    cnt = flag = 0
    abc(0)
    