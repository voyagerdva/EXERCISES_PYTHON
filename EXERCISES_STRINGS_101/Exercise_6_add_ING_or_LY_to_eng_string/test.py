import pytest
import calculate

def test_ab():
    original_string = "ab"
    result = calculate.add_string(original_string)
    ethalon = "ab"
    assert result == ethalon

def test_abc():
    original_string = "abc"
    result = calculate.add_string(original_string)
    ethalon = "abcING"
    assert result == ethalon

def test_strING():
    original_string = "strING"
    result = calculate.add_string(original_string)
    ethalon = "strINGLY"
    assert result == ethalon
