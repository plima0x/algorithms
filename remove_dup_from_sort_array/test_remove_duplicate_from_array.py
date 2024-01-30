from main import remove_duplicates


def test_remove_dup_list():
    duplicated_lists = [
        [1, 1, 1],
        [4, 4, 4, 4, 5, 5, 5],
        [7, 7, 8, 8, 8, 8, 8, 9],
        [8, 10, 11, 11, 17, 17, 17, 17, 17, 17],
        [0, 1, 2, 3, 3, 3, 3, 3, 4, 9, 9, 9]
    ]

    for current_list in duplicated_lists:
        distinct_nums = set(current_list).__len__()
        assert distinct_nums == remove_duplicates(current_list)


def test_keep_list():
    normal_lists = [
        [1],
        [4, 5],
        [7, 8, 9],
        [8, 10, 11, 12, 15],
        [0, 100, 200, 300, 500]
    ]
    for non_dup_list in normal_lists:
        current_list_len = len(non_dup_list)
        assert current_list_len == remove_duplicates(non_dup_list)


if __name__ == "__main__":
    test_remove_dup_list()
    test_keep_list()
