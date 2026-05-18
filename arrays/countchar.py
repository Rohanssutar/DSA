from collections import defaultdict, Counter

words = ["cat","bt", "hat","cac"]
chars = "ctab"
length_sum = 0

chars_hashmap = Counter(chars)
for word in words:
    cur_word = defaultdict(int)
    is_valid = True
    for ch in word:
        cur_word[ch] += 1
        if ch not in chars_hashmap or cur_word[ch] > chars_hashmap[ch]:
            is_valid = False
            break
    if is_valid:
        length_sum += len(word)

print(length_sum)