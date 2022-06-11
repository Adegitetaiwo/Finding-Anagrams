# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    word_list = list(word)
    anagram_list = list(anagram)

    # first check if all the character in anagram_list are in word_list
    comp = [char for char in anagram_list if char in word_list]

    # some characters may be for sure , so we check if they are of the same length
    if len(comp) == len(word_list):
        return True
    else:
        return False


print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
