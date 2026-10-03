n = int(input())

words = []
for i in range(n):
    words.append(input())
    
words.sort()

q = int(input())
for i in range(q):
    word = input()
    l = len(word)
    
    ini, fin = 0, n-1
    st = -1
    while ini <= fin:
        piv = (ini+fin)//2
        if word <= words[piv][:l]:
            fin = piv - 1
            st = piv
        else:
            ini = piv + 1  
    
    ini, fin = 0, n-1
    end = n
    while ini <= fin:
        piv = (ini+fin)//2
        if word < words[piv][:l]:
           fin = piv - 1
           end = piv
        else:
           ini = piv + 1 
           
    if st == -1:
        print(0)
    else:
        print(end-st)