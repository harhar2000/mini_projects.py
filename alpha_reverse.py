# Given a string str, reverse it and omit all non-alphabetic characters.

# Example
# For str = "krishan", the output should be "nahsirk".

# For str = "ultr53o?n", the output should be "nortlu".

def reverse_letter(st):
    new_str = []
    
    for letter in reversed(st):
        if letter.isalpha():
            new_str.append(letter)
            
    return "".join(new_str)