# Write a function checking whether given string contains no repeating letters, regardless of case? 
#   The function should return True if all letters are unique and False if any letter appears more than once. 
#   An empty string should also be considered valid.

def is_isogram(string):
    word = string.lower()
    checked_words = set()
    
    for letter in word:
        if letter in checked_words:
            return False
        else:
            checked_words.add(letter)
    return True