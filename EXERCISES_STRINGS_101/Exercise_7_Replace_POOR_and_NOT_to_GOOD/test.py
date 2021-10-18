import pytest
import calculate

def test_Calculate():
    original_string = 'The lyrics is not that poor!'
    result = calculate.replaceToGOOD1(original_string)
    ethalon = "The lyrics is GOOD!"
    assert result == ethalon