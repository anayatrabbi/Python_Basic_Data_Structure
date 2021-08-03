sentence = " this is a common interview question."
# find out the most frequent charecter in sentence variable
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)

char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)

print(char_frequency_sorted[1])
