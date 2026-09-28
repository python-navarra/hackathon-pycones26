n = int(input())
st = []
end = []
for i in range(n):
    a, b = list(map(int, input().split()))
    st.append(a)
    end.append(b)
    
st.sort()
end.sort()

i, j = 0, 0
can  = 0
sol = 0

while i < n:
    if st[i] < end[j]:
        i += 1
        can += 1
    else:
        j += 1
        can -= 1
    sol = max(sol, can)

print(sol)