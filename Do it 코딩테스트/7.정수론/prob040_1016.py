N, M = map(int, input().split())
square = [i**2 for i in range(2, int(M**(1/2))+1)]
print(square)