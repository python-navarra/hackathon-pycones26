n = int(input())

d = {}
max_cafe = 0
max_name = ""
for i in range(n):
    name  = input()
    
    if name not in d:
        d[name] = 1
    else:
        d[name] += 1
        
    if d[name] > max_cafe:
        max_cafe = d[name]
        max_name = name
    elif d[name] == max_cafe and max_name > name:
        max_name = name
        
print(max_name, max_cafe)