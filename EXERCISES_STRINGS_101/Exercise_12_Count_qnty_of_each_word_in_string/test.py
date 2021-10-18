import pytest
import calculate

def test_Calculate():
    original_string = "qwe qwe asd asd zxc qwe asd qwe asd zxc zxc zxc"
    result = calculate.countOccurrences(original_string)
    ethalon = {'qwe': 4, 'asd': 4, 'zxc': 4}
    assert result == ethalon