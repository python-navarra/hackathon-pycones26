import sys

sys.setrecursionlimit(10000)

n = int(input())
li = list(map(int, input().split()))

dp = [[None] * n for i in range(n)]

def solve(ini, fin):
    
    if ini > fin:
        return 0
        
    if dp[ini][fin] is not None:
        return dp[ini][fin]
   
    s1 = li[ini] - solve(ini+1, fin)
    s2 = li[fin] - solve(ini, fin-1)
    dp[ini][fin] = max(s1, s2)
    
    return dp[ini][fin]
    
print(solve(0, n-1))