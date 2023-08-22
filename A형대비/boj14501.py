## DFS
N = int(input())
consults = []
for i in range(N) :
    c, p = map(int, input().split())
    consults.append([i+1, i+c, p])
consults.sort(key=lambda x : x[1])
path = []
def abc(start) :
    global Max
    if start >= len(consults) :
        lst = [0] * (N+1)
        pay = 0
        for p in path :
            for i in range(p[0], p[1]+1) :
                if lst[i] == 1 :
                    return
                lst[i] = 1
            pay += p[2]
        
        if pay > Max :
            Max = pay 
        return
    
    for i in range(start, len(consults)) :
        if consults[i][1] > N :
            abc(len(consults))
            return
        path.append(consults[i])
        abc(i+1)
        path.pop()

Max = 0
abc(0)
print(Max)




N = int(input())

consults = []
for i in range(N) :
    c, p = map(int, input().split())
    consults.append([i+1, i+c, p])
consults.sort(key=lambda x : x[1])
while consults[-1][1] > N :
    consults.pop() 

dp = [0] * 16
for c in consults :
    if c[1] > N :
        break
    if dp[c[0]-1] + c[2] > dp[c[1]] :
        for i in range(c[1], 16) :
            dp[i] = dp[c[0]-1] + c[2]

print(dp[-1])
        
     
