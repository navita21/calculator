
import pytest

@pytest.mark.add
def test_add(cal,num1, num2):
    assert cal.add(num1,num2)==num1 +num2

@pytest.mark.sub
def test_sub(cal, num1, num2):
    assert cal.sub(num1,num2)==num1-num2


@pytest.mark.mul
def test_mul(cal, num1, num2):
    assert cal.mul(num1,num2)==num1*num2


@pytest.mark.div
def test_div(cal, num1,num2):
    assert cal.div(num1,num2)==num1 /num2
