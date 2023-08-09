import sys
input = sys.stdin.readline
def winner(lst1, lst2) :
    i = 0
    while True :
        if lst1[i] == lst2[i] :
            i += 1
        else : break
        if i == len(lst1) and i == len(lst2) :
            return 'D'
        elif i == len(lst1) :
            return 'B'
        elif i == len(lst2) :
            return 'A'
    if lst1[i] > lst2[i] :
        return 'A'
    else : 
        return 'B'
        

        

N = int(input())
for _ in range(N) :
    A, *lst_A = map(int, input().split())
    B, *lst_B = map(int, input().split())
    lst_A.sort(reverse=True)
    lst_B.sort(reverse=True)
    print(winner(lst_A, lst_B))
