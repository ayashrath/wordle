"""
This file implements the algorithm to solve the puzzle and involves the following 2 steps

1. Choose the best first word
2. Depending on the results gained from the input, choose the next word
3. Do 2 until either you loose (by giving more than 6) or you win
"""


import matplotlib.pyplot as plt
import string

words = []
frequency_dict = {}
with open("./valid-wordle-words.txt") as fh:
    for line in fh:
        word = line.strip()
        words.append(word)
        for char in word:
            char = char.lower()
            if char not in string.ascii_lowercase:
                raise ValueError
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

print(list(frequency_dict.keys()))

plt.bar(list(frequency_dict.keys()), list(frequency_dict.values()))
plt.show()
