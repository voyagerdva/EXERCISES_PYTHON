import pytest
import calculate

def test_Calculate():
    original_string_1 = "abc"
    original_string_2 = "xyz"
    result = calculate.chars_mix_up(original_string_1, original_string_2)
    ethalon = "xyc abz"
    assert result == ethalon