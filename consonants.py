def solve(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'

    subtext = []
    start = 0

    for i in range(len(word)):
        if word[i] in consonants:
            if i == 0 or word[i - 1] not in consonants:
                start = i
        else:
            if start < i:
                subtext.append(word[start:i])

    if start < len(word):
        subtext.append(word[start:])

    subtext_values = {}
    for text in subtext:
        subtext_values[text] = sum(ord(char) - ord('a') + 1 for char in text)

    return max(subtext_values.values())

print(solve("zodiacs"))
