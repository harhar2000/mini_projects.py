# Write a function taking two strings as input and returns the number of unique words that appear in both strings.
#  Words should be case-sensitive and defined as consecutive alphabetic characters. 
#  Consider using REGEX to extract words.

import re    # https://regexone.com/

def count_common_words(first, second):
    words_first = re.findall(r'[a-zA-Z]+', first)
    words_second = re.findall(r'[a-zA-Z]+', second)
    
    set_first = set(words_first)
    set_second = set(words_second)
    
    common_words = set_first.intersection(set_second)
    
    return len(common_words)



result1 = count_common_words("Yes, we all really like pizza.", "Where can we buy pizza around here?")
print(result1) 

result2 = count_common_words("There were four people at dinner.", "There were seven people at dinner.")
print(result2)  