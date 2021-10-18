import pytest
import calculate

def test_Calculate():
    original_string = 'english'
    result = calculate.lowerUpperCase(original_string)
    ethalon = ('ENGLISH', 'english')
    assert result == ethalon