def join_set(a, b, id, ran):
    if ran[b] > ran[a]:
        a, b = b, a
    ran[a] += ran[b]
    id[b] = a
    
def find_set(a, id):
    if id[a] != a:
        new_id = find_set(id[a], id)
        id[a] = new_id
    return id[a]

n = int(input())
names = input().split()

id = [i for i in range(0, n+1)]
ran = [1] * (n+1)

d = {}
con = 0
for name in names:
    if name not in d:
        con += 1
        d[name] = con

m = int(input())
for i in range(m):
    name1, name2 = input().split()
    a = d[name1]
    b = d[name2]
    
    a = find_set(id[a], id)
    b = find_set(id[b], id)
    if a != b:
        join_set(a, b, id, ran)

q = int(input())
for i in range(q):
    name = input()
    a = d[name]
    a = find_set(id[a], id)
    print(ran[a])