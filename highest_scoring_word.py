# Write a function taking a string of lowercase words that returns the word with the highest score. 
#  The score of a word is calculated by summing the values of its letters, where a = 1, b = 2, c = 3 and so on. 
#   If two words have the same score, return the word that appears first in the input string.

def high(x):
    max_score = 0
    highest_word = ""
    words = x.split()
    for word in words:
        word_score = 0
        for letter in word:
            letter_score = ord(letter) - 96
            word_score += letter_score
        if word_score > max_score:
            max_score = word_score
            highest_word = word
    return highest_word
            