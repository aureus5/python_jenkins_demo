import pytest
from src.move9 import Move9

# Test cases
Move9_test_cases = [
    [],
    [9],
    [1],
    [1,9],
    [9,1],
    [9, 9, 9, 9, 9],
    [9,1,9,1,9,1,9,1,9,1],
    [99, 34556, 23, -1234567890, -33, 9, 9999, -9],
    [-9, 3,2,4,5,-9,9, 9, -9, 9],
    [9,3,4,9,9,3,2,1],
    [99, 34556, 23, -234, -33, 9, 9999, -9],
    [9999999999, 34556, 23, -567890, -33, 9, 9999, -9]
]

@pytest.fixture
def get_obj():
    return Move9()

@pytest.mark.parametrize("list", Move9_test_cases)
def test_size_of_array(list, get_obj):
    # move9_obj = Move9()
    transformed = get_obj.move_9_to_end(list)
    if transformed is not None:
        assert len(list) == len(transformed)

@pytest.mark.parametrize("list", Move9_test_cases)
def test_int_overflow(list, get_obj):
    for num in list:
        if num > pow(2, 31) - 1 or num < -pow(2, 31):
            assert get_obj.move_9_to_end(list) is None  # list elements should be within [-2,147,483,648, 2,147,483,647]

@pytest.mark.parametrize("list", Move9_test_cases)
def test_consecutive_9_at_end_of_list(list, get_obj):
    transformed = get_obj.move_9_to_end(list)
    if transformed is not None:         # only when list is valid shall we compare transformed list
        num_of_9_ori = 0
        num_of_9_tran = 0
        for num in list:
            if num == 9:
                num_of_9_ori += 1
        for i in range(len(list) - num_of_9_ori, len(list)):  # check if the last N positions all have "9"
            if list[i] == 9:
                num_of_9_tran += 1
        assert num_of_9_ori == num_of_9_tran


@pytest.mark.parametrize("list", Move9_test_cases)
def test_none_9_items_order_kept(list, get_obj):
    transformed = get_obj.move_9_to_end(list)
    if transformed is not None:         # only when list is valid shall we compare transformed list
        none_9_ori = []
        for num in list:
            if num != 9:
                none_9_ori.append(num)
        none_9_trans = []
        for num in transformed:
            if num != 9:
                none_9_trans.append(num)
        assert none_9_ori == none_9_trans


@pytest.mark.parametrize("list", Move9_test_cases)
def test_transform_twice(list, get_obj):
    transformed = get_obj.move_9_to_end(list)
    if transformed is not None:         # only when list is valid shall we compare transformed list
        assert get_obj.move_9_to_end(transformed) is not None
        assert transformed == get_obj.move_9_to_end(transformed)