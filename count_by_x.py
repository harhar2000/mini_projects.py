# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume positive numbers only
# Return the results as an array/list

# e.g.
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]


def count_by(x, n):
    new_list = []
    
    for i in range(1, n + 1):
        new_list.append(i * x)
        
    return new_list