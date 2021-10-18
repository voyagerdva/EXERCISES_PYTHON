import pytest
import calculate

def test_Calculate():
    original_string = "0q2w4e6r8t"
    result = calculate.removeOdd(original_string)
    ethalon = "02468"
    assert result == ethalon