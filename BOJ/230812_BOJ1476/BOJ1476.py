lst = list(map(int, input().split()))
year = 0
tmp = ''
while lst != tmp :
    tmp = [year % 15 + 1, year % 28 + 1, year % 19 + 1]
    year += 1
print(year)