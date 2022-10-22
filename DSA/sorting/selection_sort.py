def selection_sort(array):

    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j

        array[i], array[min] = array[min], array[i]

    return array
            

if __name__ == '__main__':
    # Test
    test_list = [50, 46, 29, 103, 50302, 1]
    print(selection_sort(test_list))