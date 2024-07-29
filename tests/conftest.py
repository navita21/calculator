from source.calculator import Calculator
import pytest 

@pytest.fixture(scope="module")
def cal():
    return Calculator()

def pytest_addoption(parser):
    parser.addoption("--num1", action="store", default=1, type=int, help="First number")
    parser.addoption("--num2", action="store", default=1, type=int, help="Second number")

@pytest.fixture
def num1(request):
    return request.config.getoption("--num1")

@pytest.fixture
def num2(request):
    return request.config.getoption("--num2")