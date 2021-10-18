import pytest
import calculate

def test_Calculate():
    original_string = "google.com"
    result = calculate.char_frequency(original_string)
    ethalon = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
    assert result == ethalon