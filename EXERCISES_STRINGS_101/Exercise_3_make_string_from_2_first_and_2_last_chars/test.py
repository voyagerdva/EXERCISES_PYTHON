import pytest
import calculate

def test_CalculateFullString():
    original_string = "w3resource"
    result = calculate.
    ethalon =
    assert result == ethalon

def test_Calculate2chars():
    original_string = "google.com"
    result = calculate.char_frequency(original_string)
    ethalon = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
    assert result == ethalon

def test_CalculateLess2Chars():
    original_string = "google.com"
    result = calculate.char_frequency(original_string)
    ethalon = {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
    assert result == ethalon
