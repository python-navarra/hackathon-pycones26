a, b = map(int, input().split())

m = a
while m % b != 0:
    m += a

print(m)