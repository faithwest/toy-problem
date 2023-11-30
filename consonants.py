# Define a function to find the highest value of consonant substrings in a word
def solve(word):
    # List of consonants
    consonants = 'bcdfghjklmnpqrstvwxyz'

    # Initialize an empty list to store consonant substrings
    subtext = []
    start = 0

    # Iterate through each character in the word
    for i in range(len(word)):
        # Check if the character is a consonant
        if word[i] in consonants:
            # Check if it's the first consonant or follows a non-consonant
            if i == 0 or word[i - 1] not in consonants:
                start = i
        else:
            # Check if there is a consonant substring before the current character
            if start < i:
                subtext.append(word[start:i])

    # Check if there is a consonant substring at the end of the word
    if start < len(word):
        subtext.append(word[start:])

    # Calculate values for each consonant substring
    subtext_values = {}
    for text in subtext:
        subtext_values[text] = sum(ord(char) - ord('a') + 1 for char in text)

    # Return the maximum value among the consonant substrings
    return max(subtext_values.values())

# Example usage
print(solve("zodiacs"))
