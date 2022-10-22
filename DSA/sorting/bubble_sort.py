def bubble_sort(array):

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i] , array[j] = array[j], array[i]

    return array


if __name__ == '__main__':
    # Test
    test_list = [50, 46, 29, 103, 50302, 1]
    print(bubble_sort(test_list))