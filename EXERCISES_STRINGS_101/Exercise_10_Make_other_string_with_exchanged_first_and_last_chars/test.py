import pytest
import calculate

def test_Calculate():
    original_string = "PkjlkjlkjlkjlO"
    result = calculate.makeString(original_string)
    ethalon = "OkjlkjlkjlkjlP"
    assert result == ethalon