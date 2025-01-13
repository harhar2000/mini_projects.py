# Write a function finding the longest strict palindrome in a given string.
#   Where the palindrome reads exactly the same forwards and backwards, 
#   respecting letter case and all characters?


def find_longest_strict_palindrome(input_string):
    longest_palindrome = ""
    
    for start in range(len(input_string)):
        for end in range(start + 1, len(input_string) + 1):
            substring = input_string[start:end]
            if substring == substring[::-1]:
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
    
    return longest_palindrome

print(find_longest_strict_palindrome("bob has a racecar"))
print(find_longest_strict_palindrome("bob has a racecar and a bike"))
print(find_longest_strict_palindrome("anna arrived at noon"))
