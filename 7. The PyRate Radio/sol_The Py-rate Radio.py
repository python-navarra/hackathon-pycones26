s = input()
n = int(input())

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

caesar_s = ''
for c in s:
    if c in lower_case:
        idx = lower_case.find(c)
        caesar_s += lower_case[(idx+n)%26]
    elif c in upper_case:
        idx = upper_case.find(c)
        caesar_s += upper_case[(idx+n)%26]
    else:
        caesar_s += c

print(caesar_s) 