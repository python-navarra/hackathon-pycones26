def gcd(a, b):
    if a == 0:
        return b
    a, b = b%a, a
    return gcd(a, b)

a, b = list(map(int, input().split()))

print(a*b//gcd(a, b))