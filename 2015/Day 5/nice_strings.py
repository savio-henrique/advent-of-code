input = open("input.txt").read().split("\n")

nice_counter = 0
#Part 1#
# def isNice(string):
#     if ((string.count("ab") >= 1) or (string.count("cd") >= 1) or
#         (string.count("pq") >= 1) or (string.count("xy") >= 1)):
#         return False
#     vowel_count = sum([1 for letter in string if letter in "aeiou"])
#     double_letters = bool({True for letter in string if string.count(f"{letter}{letter}") >= 1})
#     if (vowel_count < 3) or not double_letters:
#         return False
#     return True
#
#Part 1#
#Part 2#
def isNice(string):
    pairs = bool({True for i in range(len(string) - 1) if string.count(string[i:i+2]) >= 2})
    repeats = bool({True for i in range(len(string) - 2) if string[i] == string[i + 2]})
    return pairs and repeats
#Part 2#

for string in input:
    if isNice(string):
        nice_counter += 1

print(nice_counter) #Part 1 and 2 Solution

