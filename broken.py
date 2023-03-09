# Fixed indenting from 3 to 4 spaces
def quick_sort(numbers):
    quick_sort_helper(numbers, 0, len(numbers)-1)

def quick_sort_helper(numbers, first, last):
    if first<last:

        splitpoint = partition(numbers, first, last)

        quick_sort_helper(numbers, first, splitpoint-1)
        quick_sort_helper(numbers, splitpoint+1, last)

def partition(numbers, first, last):
    pivotvalue = numbers[last] # Swapped to last

    # Swapped from first + 1 to last - 1
    leftmark = first
    rightmark = last - 1

    # Removed if and - 1. Have to check while right is bigger than left 
    # While pointers don't overlap 
    while rightmark > leftmark: 

        # left has to be smaller than last can't go over list length
        # Same for right but swapped.
        # This caused the original index error (The setup)
        # Remove = and change out rightmark, similar for rightmark
        while leftmark < last and numbers[leftmark] < pivotvalue: 
            leftmark += 1 # Change to += 

        while rightmark > first and numbers[rightmark] >= pivotvalue: # Remove =
            rightmark -= 1 # Change to -=

        # Swapping values in the iteration
        if rightmark > leftmark: # Set up new if same as above
            temp = numbers[leftmark]
            numbers[leftmark] = numbers[rightmark]
            numbers[rightmark] = temp

    if numbers[leftmark] > pivotvalue: # Need this if statement
        temp = numbers[leftmark]
        numbers[leftmark] = numbers[last]
        numbers[last] = temp

    return leftmark # Need to return leftmark (new split point)

numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("Before Sort: {}".format(numbers))
quick_sort(numbers)
print("After Sort: {}".format(numbers))

# This was only possible with some research on the algorithm.
# Need to understand it to fix it.