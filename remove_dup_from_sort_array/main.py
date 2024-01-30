def remove_duplicates(nums):
    """
    Remove in-place the duplicated elements in the ordered list nums.
    :param nums: An ordered list with duplicated elements.
    :return: The number of distinct elements in the list.
    """
    # store the original length of the list.
    original_len = len(nums)
    # The goal is to find duplicated elements and substitute them with the next different elements.
    # Therefore, switch_index will store the index of the next elements to compare with the current element.
    switch_index = 1
    # The current element in the list.
    current_index = 0
    # The number of distinct elements in the list. The list must have one distinct element at least.
    qtd_distinct_nums = 1
    # Loop while there is element in the list to compare with.
    while switch_index < len(nums):

        # If the current element is equal to the next element, increment the switch_index and compare again.
        # when a different element is found, then store its value next to the current element.

        if nums[current_index] == nums[switch_index]:
            switch_index += 1
            continue
        # Initially, the switch_index will point to the next element in the list.
        # If it is not true, this means that the switch_index needed to be incremented to search for an element
        # different from the current element.
        elif current_index + 1 < switch_index:
            # change the value of the element next to the current element.
            # example: list is [1, 1, 2], current_element is 1,
            # so [1, 1, 2], will turn into [1, 2, 2] and we will remove the last 2 in the end of the loop.
            nums[current_index + 1] = nums[switch_index]
        # increment all the index and compare again in the next loop.
        current_index += 1
        switch_index += 1
        # increase the number of distinct elements.
        qtd_distinct_nums += 1

    # Verify if the number of distinct elements is the same as the length of the list.
    # If not, that is because the list contain duplicated elements at the final, and it must be removed.
    if qtd_distinct_nums < original_len:
        count_nums_remove = original_len - qtd_distinct_nums
        while count_nums_remove > 0:
            nums.pop()
            count_nums_remove -= 1

    # Return the length of the list. It now will have only distinct elements.
    return len(nums)

