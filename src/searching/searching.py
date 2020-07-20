def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
       if arr[i] == target:
           return i

    return -1 # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #define the range
    low = 0
    high = len(arr) -1
    middle = 0

    while low <= high:
        middle = low + ((high - low) // 2)
        # compare middle value to target value to see if target is present at middle
       # if target is smaller, ignore right half of arr  
        if arr[middle] > target:
            high = middle -1
        # If target is greater, ignore left half of arr
        elif arr[middle] < target:
            low = middle + 1
        else:
            return middle
    return -1  # not found

