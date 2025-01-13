# Write a function taking a string of directions (`N`, `S`, `E`, `W`) representing a robot's movements on a grid. 
# The robot starts at the origin `(0, 0)`
# and moves one step in the specified direction for each character in the string. 
# Ignore any invalid characters. 
# The function should return the number of unique locations the robot visits more than once.
# Test the function with inputs 'NS', 'WEWNES', and 'SxWxNxN'



def count_revisited_locations(directions):
    x, y = 0, 0
    visited = set()  
    revisited_locations = set()  
    
    visited.add((x, y))
    
    for move in directions:
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        else:
            continue  

        if (x, y) in visited:
            revisited_locations.add((x, y)) 
        else:
            visited.add((x, y))  

    return len(revisited_locations)  

print(count_revisited_locations("NS"))  
print(count_revisited_locations("WEWNES"))  
print(count_revisited_locations("SxWxNxN"))  
