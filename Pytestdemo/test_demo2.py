import pytest


def test_m2case1():
    print("hello world!")


@pytest.mark.smoke
# @pytest.mark.smoke marks this method as smoke.
# This should be used when you want to run cases marked with a given keyword. In this case it's smoke.
# Use this keyword for smoke and regression testing.
def test_m2case2():
    print("2+4 is 6")
