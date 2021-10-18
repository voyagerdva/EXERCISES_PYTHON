import pytest
import calculate

def test_Calculate():
    original_string = "asfd,bcd,dll,lkj,ass,dsd,cad"
    result = calculate.sortedList(original_string)
    ethalon = "asfd, ass, bcd, cad, dll, dsd, lkj"
    assert result == ethalon