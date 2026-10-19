n = int(input())

root = 0
trie = [[0, {}]]
for i in range(n):
    word = input()
    
    pos = root
    for c in word:
       if c not in trie[pos][1]:
           trie[pos][1][c] = len(trie)
           trie.append([0, {}])
       pos = trie[pos][1][c]
       trie[pos][0] += 1

q = int(input())
for i in range(q):
    word = input()
    
    pos = root
    sol = 0
    for c in word:
        if c not in trie[pos][1]:
            sol = 0
            break
        pos = trie[pos][1][c]    
        sol = trie[pos][0]    
    
    print(sol)