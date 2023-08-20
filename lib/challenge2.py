
# Challenge 2: Two numbers are positive.
# Task:
# Your job is to write a function, which takes three integers 
# a, b, and c as arguments, and returns True if exactly two of 
#of the three integers are positive numbers (greater than zero), 
#and False - otherwise.

# Examples:
# (2, 4, -3) == True

# (-4, 6, 8) == True

# (4, -6, 9) == True

# (-4, 6, 0) == False

# (4, 6, 10) == False

# (-14, -3, -4) == False

def two_possitive(a, b, c):
    count = 0

    if a > 0:
        count += 1
    if b > 0:
        count +=1
    if c > 0:
        count += 1

    
    if count == 2:
        print(True)
    else:
        print(False)
    


two_possitive(2, 3, 4) #False
two_possitive(2, 4, -3) #True
two_possitive(-4, 6, 0) #False
two_possitive(4, -6, 9) #True
two_possitive(-14, -3, -4) #False



