import pytest

import TestDay1


@pytest.mark.xfail
# @pytest.mark.xfail runs this method during execution but won't show as a result.
# This should be used when you don't need to run this case but other case is dependent on this case.
def test_case1():
    print("Hello")


@pytest.mark.skip
# @pytest.mark.skip skips this method during execution.
# This should be used when you don't need to run this case.
def test_case2():
    assert "Krishna" in TestDay1.title

def test_crossBrowser(crossBrowser):
    print(crossBrowser)
