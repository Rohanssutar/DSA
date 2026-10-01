s, t = 'coaching','coding'
count = 0

for i in range(len(t)):
    if not t[i] in s:
        s += t[i:]
        count += 1

print(len(s), len(t))