n = int(input())
a = [0] * 10005
for i in range(n):
    ini, fin = list(map(int, input().split()))
    a[ini]+=1
    a[fin]-=1

sol = a[0]
for i in range(1, 10001):
    a[i] += a[i-1]
    sol = max(sol, a[i])
    
print(sol)