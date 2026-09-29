n = int(input())

l = []
for i in range(n):
    name  = input()
    l.append(name)

l.sort()
sol_name = l[0]
can = 1
sol_can = 1
for i in range(1, n):
    if l[i] == l[i-1]:
        can += 1
    else:
        can = 1
    if can > sol_can or (can == sol_can and l[i] < sol_name):
        sol_can = can
        sol_name = l[i]

print(sol_name, sol_can)