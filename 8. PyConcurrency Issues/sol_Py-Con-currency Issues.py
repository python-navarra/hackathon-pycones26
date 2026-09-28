n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort(key=lambda x: x[1])

sol = 0
end = 0
for i in range(n):
    if end <= a[i][0]:
        sol += 1
        end = a[i][1]
        
print(sol)