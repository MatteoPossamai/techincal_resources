def insertion_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array

if __name__ == '__main__':
    # Test
    print('PRE ORDERING')
    test_list = [50, 46, 29, 103, 50302, 1]
    print(test_list)
    print("POST ORDERING")
    print(insertion_sort(test_list))