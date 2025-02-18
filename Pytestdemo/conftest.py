import pytest


@pytest.fixture(scope="class")
def setup():
    print("\nsetup")
    yield
    print("prints last")


@pytest.fixture(name="dataload")
def dataload():
    print("data driven fixture")
    return ["apple","banana", "fruits.com"]

@pytest.fixture(params=["chrome", "firefox","safari"])
def crossBrowser(request):
    return request.param

