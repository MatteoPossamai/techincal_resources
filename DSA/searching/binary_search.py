"""
Checks if a given element is present in a list or not.
"""

# My own version
def binary_search(array, element):
    index = int(len(array) / 2)
    
    if array[index] == element:
        return True
    elif index == 0:
        return False
    elif array[index] < element:
        return binary_search(array[index:], element)
    elif array[index] > element:
        return binary_search(array[:index], element)

# GeeksForGeeks version
def binarySearch(array, target): 
    low = array[0]
    high = array[len(array)-1]
    if array[0] == target:
            return 0
    elif array[len(array)-1] == target:
        return len(array)-1
    else:
        while(low <= high):
            mid = int((low+high)/2)
            if array[mid]==target:
                return mid
            elif array[mid] > target:
                high = mid -1
            elif array[mid] < target:
                low = mid +1
        return -1 

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Testing
    print("HERE SHOULD BE TRUE")
    print(binary_search(l, 1))
    print(binary_search(l, 2))
    print(binary_search(l, 3))
    print(binary_search(l, 4))
    print(binary_search(l, 5))
    print(binary_search(l, 6))
    print(binary_search(l, 7))
    print(binary_search(l, 8))
    print(binary_search(l, 9))
    print("HERE SHOULD BE FALSE")
    print(binary_search(l, 10))
    print(binary_search(l, -1))
    print(binary_search(l, 50))