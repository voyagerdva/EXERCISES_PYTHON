import pytest
import calculate

def test_Calculate():
    original_string = "tetragramatron"
    result = calculate.change_char(original_string)
    ethalon = "te$ragrama$ron"
    assert result == ethalon