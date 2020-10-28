

s = input("input word: ")

for i in range(len(s)):
    if s[i] == s[-i]:
        break

