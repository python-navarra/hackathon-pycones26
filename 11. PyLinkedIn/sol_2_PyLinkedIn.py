from collections import deque


def add_edge(nod, new_nod, g):
    if nod not in g:
        g[nod] = []
    g[nod].append(new_nod)

n = int(input())
names = input().split()

m = int(input())
g = {}
for i in range(m):
    name1, name2 = input().split()
    add_edge(name1, name2, g)
    add_edge(name2, name1, g)
    
sol = {}
for name in names:
    if name not in sol:
        q = deque([name])
        
        nod_visit = set()
        while q:
            nod = q.popleft()
            
            if nod in nod_visit:
                continue
            
            nod_visit.add(nod)
            if nod in g:
                for new_nod in g[nod]:
                    if new_nod not in nod_visit:
                        q.append(new_nod)
        
        for nod in nod_visit:
            sol[nod] = len(nod_visit)    

q = int(input())
for i in range(q):
    name = input()
    print(sol[name])
    