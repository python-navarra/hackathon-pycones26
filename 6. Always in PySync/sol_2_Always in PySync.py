a, b = list(map(int, input().split()))

mcm = max(a, b)
while mcm % a != 0 or mcm % b != 0:
    mcm += 1

print(mcm)