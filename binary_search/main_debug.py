def binary_search(num_list, target):
    """
    Verify if the number specified in target parameter is in the list num_list using binary search.
    :param num_list: An ordered list of numbers.
    :param target: The number that will be searched in the list.
    :return: the index of the target number, or -1 if target is not in the list.
    """

    low_index = 0

    high_index = len(num_list) - 1
    while low_index <= high_index:

        mean_index = (low_index + high_index) // 2
        print(f"Current mean index: {mean_index}, current value: {num_list[mean_index]}")
        print(f"Low index: {low_index}, high index: {high_index}\n")
        if num_list[mean_index] < target:
            low_index = mean_index + 1
        elif num_list[mean_index] > target:
            high_index = mean_index - 1
        else:
            return mean_index

    return -1


NUM_LIST = [number for number in range(100, 201)]
num_target = 101
print(binary_search(NUM_LIST, num_target))

