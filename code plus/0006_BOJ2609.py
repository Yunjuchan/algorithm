n1, n2 = map(int, input().split())
if n1 >= n2 :
    big = n1
    small = n2
else :
    big = n2
    small = n1
tmp = None
while small != 0 :
    tmp = small
    small = big % tmp
    big = tmp
gcd = big
lcm = n1 * n2 // gcd
print(gcd)
print(lcm)