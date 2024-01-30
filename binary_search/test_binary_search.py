from main import binary_search
from random import choice


NUM_LIST = [number for number in range(0, 101)]


def test_found_item():
    num_target = choice(NUM_LIST)
    target_index = binary_search(NUM_LIST, num_target)
    assert target_index != -1


def test_found_item_in_first_half():
    num_target = 33
    target_index = binary_search(NUM_LIST, num_target)
    assert target_index != -1


def test_found_item_in_second_half():
    num_target = 88
    target_index = binary_search(NUM_LIST, num_target)
    assert target_index != -1


def test_item_not_found():
    num_target = 103
    target_index = binary_search(NUM_LIST, num_target)
    assert target_index == -1


if __name__ == "__main__":
    test_found_item()
    test_found_item_in_first_half()
    test_found_item_in_second_half()
    test_item_not_found()
