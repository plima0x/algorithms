from typing import List


def binary_search(num_list: List[int], target: int):
    """
    Verify if the number specified in target parameter is in the list num_list using binary search.
    :param num_list: An ordered list of numbers.
    :param target: The number that will be searched in the list.
    :return: the index of the target number, or -1 if target is not in the list.
    """

    # Get the current lowest and higher indexes in the list.
    low_index = 0
    high_index = len(num_list) - 1

    # Continue searching until the lower index and the higher index are different or the target index is found.
    while low_index <= high_index:
        # Instead of searching the list from the first element to the last, get the element
        # in the middle of the list and compare if the element is less or higher than the target element.

        mean_index = (low_index + high_index) // 2
        # If the element in the middle is lower than the target element, then the target element may be in the 
        # second half of the list. So, now search the middle element again, but starting from 
        # the second half of the list.
        if num_list[mean_index] < target:
            low_index = mean_index + 1
        # If the element in the middle is higher than the target element, then the target element may be in
        # the first half of the list. So, now search the middle element again, but starting from 
        # the first half of the list.
        elif num_list[mean_index] > target:
            high_index = mean_index - 1
        else:
            # Otherwise, the target element was found and return the index of it.
            return mean_index
    # If the element was not found in the list, return -1.
    return -1


