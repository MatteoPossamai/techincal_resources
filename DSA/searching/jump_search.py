import math

def jump_search( arr , x , n ):
    step = math.sqrt(n) 
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
     
    # Doing a linear search for x in
    # block beginning with prev.
    while arr[int(prev)] < x:
        prev += 1
         
        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1
     
    # If element is found
    if arr[int(prev)] == x:
        return prev
     
    return -1

if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    element = 42
    print(jump_search(lista, element, len(lista)))