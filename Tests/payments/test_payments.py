import pytest
from configparser import ConfigParser
import json
import requests
import jsonpath

from Configurations.commons.CommonFunctions import CommonFunc
from Configurations.commons.HelperFunctions import HelperFuncs
from Configurations.commons.Logger import LOGGER

config = ConfigParser()

@pytest.fixture(autouse=True)
def readConfigDatas():
    config.read("/Users/olayodeolatunji/pythonProject/ApiTesting/SquareApi/Configurations/Config.cfg")


# @pytest.mark.usefixtures("readConfigDatas", "getAuths")
class Test_PaymentApi(CommonFunc):

    def __int__(self):
        self.config = ConfigParser()

    def test_createGetRequest(self, getAuths):
        print(config.get("payments", "geturl"))
        print(getAuths)
        response = requests.get(config.get("payments", "geturl"), headers=getAuths)
        jsonResponse = json.loads(response.content)
        print(jsonResponse)
        assert response.status_code == HelperFuncs.STATUS200()


    def test_createPostRequest(self, getAuths):
        global id
        file = HelperFuncs.openFiles("/Users/olayodeolatunji/pythonProject/ApiTesting/SquareApi/Configurations/createpayments.json")
        body = file.read()
        # body['idempotency_key'] = item
        response = requests.post(config.get("payments", "createpaymenturl"), data=body, headers=getAuths)
        jsonResponse = json.loads(response.content)
        id = jsonpath.jsonpath(jsonResponse, "payment.id")
        assert response.status_code == HelperFuncs.STATUS200()
        assert id[0] is not False

    def test_getPaymentById(self, getAuths):
        response = requests.get(config.get("payments", "geturl") + "/" + str(id[0]), headers=getAuths)
        jsonResponse = json.loads(response.content)
        assert response.status_code == HelperFuncs.STATUS200()
        returnedId = jsonpath.jsonpath(jsonResponse, "payment.id")
        assert returnedId[0] == id[0]

    def test_createPutRequest(self, getAuths):
        file = HelperFuncs.openFiles("/Users/olayodeolatunji/pythonProject/ApiTesting/SquareApi/Configurations/updatepayment.json")
        body = file.read()
        response = requests.put(config.get("payments", "geturl") + "/" + str(id[0]), data=body, headers=getAuths)
        jsonResponse = json.loads(response.content)
        bodys = json.loads(body)
        updatedTime = jsonpath.jsonpath(jsonResponse, "payment.updated_at")
        currency = jsonpath.jsonpath(jsonResponse, "payment.amount_money.currency")
        assert response.status_code == HelperFuncs.STATUS200()
        assert currency[0] == bodys["payment"]["amount_money"]["currency"]

    def test_completePayment(self, getAuths):
        response = requests.post(config.get("payments", "geturl") + "/" + str(id[0]) + "/complete", headers=getAuths)
        jsonResponse = json.loads(response.content)
        status = jsonpath.jsonpath(jsonResponse, "payment.status")
        if response.status_code == HelperFuncs.STATUS200():
            assert status[0] == "COMPLETED"
        else:
            LOGGER.log().info("Complete payment returned error")
            raise ValueError(f"EXPECTED STATUS CODE 200, GOT {response.status_code}")

    def test_createDeleteRequest(self, getAuths):
        pass


