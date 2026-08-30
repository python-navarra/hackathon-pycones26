s, *l = list(input().split())
l = list(map(int, l))
if s == "triangle":
    print(sum(l))
else:
    print(4 * l[0])
