a, b = list(map(int, input().split()))

ta = a
tb = b
while ta != tb:
    if ta < tb:
        ta += a
    else:
        tb += b
    
print(ta)