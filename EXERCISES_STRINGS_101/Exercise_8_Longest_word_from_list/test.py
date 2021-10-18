import pytest
import calculate

def test_Calculate():
    original_list = ["qwe", "qwert", "qwertyu", "qwert", "aa", "sdfsdfsdfsdfsdf", "s", "d", ""]
    result = calculate.longestWord(original_list)
    ethalon = ('sdfsdfsdfsdfsdf', 15)
    assert result == ethalon