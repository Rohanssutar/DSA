allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
count = 0

hashmap = {}
for ch in allowed:
    hashmap[ch] = 1 + hashmap.get(ch, 0)

for word in words:
    is_consistent = True
    for ch in word:
        if ch not in hashmap:
            is_consistent = False
            break
    if is_consistent:
        count += 1

print(count)