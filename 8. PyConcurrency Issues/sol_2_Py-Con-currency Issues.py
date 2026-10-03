n = int(input())
eve = {}
for i in range(n):
    a, b = list(map(int, input().split()))
    if b not in eve:
       eve[b] = []
    eve[b].append([a, b])
    
sol = 0
pos = 0
for i in range(10001):
    if i in eve:
        for e in eve[i]:
            if e[0] >= pos:
                pos = e[1]
                sol += 1
                break
                
print(sol)
