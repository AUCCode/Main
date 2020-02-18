"""

Simple list sorting algorithim | Bubble Sort
Written by RSimon for the AUC Code Club

"""

list_of_numbers = [ 1, 4, 2, 56, -50, 32, 100, -200, 40 ] # creates a list variable with a set of unordered numbers


#   First iterative loop --- This 'for loop' will run through the list the same amount of times as there are elements in the list

for I in range( len( list_of_numbers ) ): 

#   Second iterative loop ---  This 'for loop' will run through the list the same amount of times as there are elements in the list minus one

#   The minus one here is important because it allows us to check every element in the list without encountering a 'Index out of range' error

    for s in range( len( list_of_numbers ) - 1 ):
        
#   Main 'if statement' --- This next few lines of code will check each element of the list to see whether or not the element before the next element is greater or less than it.

        if list_of_numbers[s] > list_of_numbers[s+1]: # Compares the sth term with the sth + 1 term. For example, it will check the 3rd element with the 4th
            
            list_of_numbers[s], list_of_numbers[s+1] =  list_of_numbers[s+1], list_of_numbers[s] # This is a "Pythonic" way of swapping variable. It basically tells the computer to swith the values of the two elements
            

            
print(list_of_numbers) # Prints the new sorted list.





