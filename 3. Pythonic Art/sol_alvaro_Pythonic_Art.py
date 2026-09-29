inp = input().split()
fig = inp[0]

if fig == "triangle" or fig == "triangulo":
    a = int(inp[1])
    b = int(inp[2])
    c = int(inp[3])
    p = a + b + c
else:
    side = int(inp[1])
    p = 4 * side

print(p, end="")
