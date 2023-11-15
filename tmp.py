N=1000-int(input())
A=500,100,50,10,5,1
c=0
for i in A:x,N=divmod(N,i);c+=x
print(c)