st ='BTSKR'
num = int(input())
cnt=0
def abc(level,used):
    global cnt
    if level==num:
        if used[2] == True :
            cnt+=1
        return
    for i in range(5):
        if used[i]==1:
            continue
        path[level]=st[i]
        used[i]=1
        abc(level+1,used)
        used[i]=0
path = ['']*num
used = [0]*5
abc(0,used)
print(cnt)

