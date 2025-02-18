import pytest
from Pytestdemo.BaseClass import BaseClass

@pytest.mark.usefixtures("dataload")
class TestExample(BaseClass):
    def test_editprofile(self,dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])
