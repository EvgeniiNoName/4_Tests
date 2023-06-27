import pytest
from task2 import new_folder

@pytest.mark.parametrize(
        "status_code_, path, token_YA",[
            (201, 'New_folder_for_test', "1"),
            (401, 'New_folder_for_test', "123"),
            (409, 'New_folder_for_test', "1)
            ])
def test_new_folder(status_code_, path, token_YA):
    # expected =
    res = new_folder(token_YA, path).status_code
    assert res == status_code_