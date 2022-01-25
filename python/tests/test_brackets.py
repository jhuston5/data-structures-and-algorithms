from stack_queue.stack import Stack
from stack_queue.brackets import validate_brackets
import pytest

# Test True when passing in a correct string
def test_correct_string():
    expected = validate_brackets("(({{}}))")
    assert expected == True


# Test False when passing in an incorrect string
def test_incorrect_string():
    expected = validate_brackets("(({{}}){")
    assert expected == False


# Test True when passing in extra characters (Not Brackets)
def test_extra_char_string():
    expected = validate_brackets("(({{charlotte}}))")
    assert expected == True
