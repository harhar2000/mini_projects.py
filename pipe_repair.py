# Write a function taking a sorted list of unique numbers and returns a new list 
#   where all missing numbers are filled in, 
#   ensuring the sequence increments by 1 from the smallest number to the largest number.

# For example:

# Input: [1, 3, 5, 6, 7, 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]


def pipe_fix(nums):
    first = nums[0]
    last = nums[-1]

    return list(range(first, last + 1))


print(pipe_fix([1, 3, 5, 6, 7, 8]))