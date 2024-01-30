def remove_duplicates(nums):
    original_len = len(nums)
    switch_index = 1
    current_index = 0
    qtd_distinct_nums = 1
    print(f"list before the removing items: {nums}")
    while switch_index < len(nums):
        if nums[current_index] == nums[switch_index]:
            switch_index += 1
            continue
        elif current_index + 1 < switch_index:
            nums[current_index + 1] = nums[switch_index]
        current_index += 1
        switch_index += 1
        qtd_distinct_nums += 1

    if qtd_distinct_nums < original_len:
        count_nums_remove = original_len - qtd_distinct_nums
        while count_nums_remove > 0:
            nums.pop()
            count_nums_remove -= 1
    print(f"list after the removing items: {nums}")
    print(f"Number of distinct elements: {len(nums)}")
    return len(nums)


duplicated_lists = [
    [1, 1, 1],
    [4, 4, 4, 4, 5, 5, 5],
    [1, 2, 3],
]

for current_list in duplicated_lists:
    count_distinct = remove_duplicates(current_list)

