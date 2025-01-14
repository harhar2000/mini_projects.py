# Write a function checking if a password is valid. A valid password must meet the following criteria:

# It must be at least 8 characters long.
# It must contain at least one of the following special characters: !, @, $, %, &.
# Return True if the password is valid, otherwise return False.

def is_valid(password):
    if len(password) >= 8:
        for char in ['!', '@', '$', '%', '&']:
            if char in password:
                return True
        return False
    return False

print(is_valid("1234567"))
print(is_valid("12345678"))
print(is_valid("12345!78"))