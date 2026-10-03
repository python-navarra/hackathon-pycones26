n = int(input())

sol = {}
for i in range(n):
    word = input()
    
    hash_ = ""
    for c in word:
        hash_ += c
        if hash_ not in sol:
            sol[hash_] = 0
        sol[hash_] += 1
        
q = int(input())
for i in range(q):
    word = input()
    if word in sol:
        print(sol[word])
    else:
        print(0)