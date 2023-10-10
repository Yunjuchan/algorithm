import sys
input = sys.stdin.readline
def find(x) :
    global friends
    if not friends.get(x, '') :
        friends[x] = x
        L[x] = 1
        return friends[x]
    if friends[x] == x :
        return friends[x]
    friends[x] = find(friends[x])
    return friends[x]

def union(a, b) :
    fa, fb = map(find, (a, b))
    if fa == fb :
        return L[fa]
    L[fa] += L[fb]
    friends[fb] = friends[fa]
    return L[fa]
    
T = int(input())
for tc in range(T) :
    N = int(input().rstrip())
    friends = {}
    L = {}
    for _ in range(N) :
        a, b = input().split()
        ret = union(a, b)
        print(ret)
        
        