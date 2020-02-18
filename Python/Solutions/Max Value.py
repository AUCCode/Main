"""

Max Value finding algorithim | Linear Search
Written by RSimon for the AUC Code Club

"""


list_of_numbers = [ 1, 4, 2, 56, -50, 32, 100, -200, 40 ] # creates a list variable with a set of unordered numbers

max_value = list_of_numbers[0] # Assumes the largest value in the list is the first value


for i in range(len(list_of_numbers)): # This "for-loop" will go over every value in the list provided
    
    if list_of_numbers[i] > max_value: # This "if-statement" checks each value in the list against the current max value

        max_value = list_of_numbers[i] # changes the max value if and only if the old max is less than the new max


print(max_value) # Prints max value
