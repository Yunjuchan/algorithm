N = int(input())
cnt = N
for i in range(2, int(N**(1/2))+1) :
    if N % i == 0 :
        cnt -= cnt // i
        while N % i == 0 :
            
            N //= i 
if N != 1 :
    cnt -= cnt // N    
print(cnt)
