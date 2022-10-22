"""
Checks if a given element is present in a list or not.
"""

def linear_search(list, element):
    """
    Returns the index of the element if present in the list, else returns -1.
    """
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    element = 4
    print(linear_search(list, element))