MOD = 10**9 + 7
H1 = 31
H2 = 37
sol = {}

n = int(input())
for i in range(n):
    word = input()
    
    h1 = 0
    h2 = 0
    for c in word:
        h1 = (h1 * H1 + ord(c)) % MOD
        h2 = (h2 * H2 + ord(c)) % MOD
        
        hash_ = (h1, h2)
        if hash_ not in sol:
            sol[hash_] = 0
        sol[hash_] += 1
        
q = int(input())
for i in range(q):
    word = input()
    
    h1 = 0
    h2 = 2
    for c in word:
        h1 = (h1 * H1 + ord(c)) % MOD
        h2 = (h2 * H2 + ord(c)) % MOD
    hash_ = (h1, h2)
    
    if hash_ in sol:
        print(sol[hash_])
    else:
        print(0)