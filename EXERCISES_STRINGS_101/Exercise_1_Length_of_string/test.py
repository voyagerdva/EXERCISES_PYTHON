import pytest
import calculate

def test_Calculate():
    original_string = "w2resource.com"
    result = calculate.string_length(original_string)
    ethalon = 14
    assert result == ethalon