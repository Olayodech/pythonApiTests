import pytest
from configparser import ConfigParser

config = ConfigParser()

@pytest.fixture()
def getAuths(readConfigData):
    print(readConfigData)
    auth = {"Authorization": 'Bearer ' + config.get("userdata", "bearer-token"), "Content-Type": "application/json"}
    return auth

@pytest.fixture(autouse=True)
def readConfigData():
    config.read("/Users/olayodeolatunji/pythonProject/ApiTesting/SquareApi/Configurations/Config.cfg")
