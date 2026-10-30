s = input()
k = int(input())

caesar_s = ''
for c in s:
    if 'a' <= c <= 'z':
        caesar_s += chr(ord('a') + (ord(c) - ord('a') + k) % 26)
    elif 'A' <= c <= 'Z':
        caesar_s += chr(ord('A') + (ord(c) - ord('A') + k) % 26)
    else:
        caesar_s += c

print(caesar_s) 