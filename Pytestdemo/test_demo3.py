import pytest


# @pytest.fixture()
# def setup():
#     print("\nsetup")
#     yield
#     print("prints last")

@pytest.mark.usefixtures("setup")
class Testexample:

    def testcase_fixture1(self):
        print("Execute steps in fixturedemo1 method")

    def testcase_fixture2(self):
        print("Execute steps in fixturedemo2 method")

    def testcase_fixture3(self):
        print("Execute steps in fixturedemo3 method")

    def testcase_fixture4(self):
        print("Execute steps in fixturedemo4 method")