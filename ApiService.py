import requests
from enum import Enum, auto

class RefereeDecision(Enum):
    WHITE = 0
    RED = 1
    BLUE = 2
    YELLOW = 3

class RefereeType(Enum):
    MAIN = "F"
    LEFT = "L"
    RIGHT = "R"

class ApiService:
    token = None
    competitionId = None
    attemptLogId = None

    baseUrl = "https://heavyplates.com/api"
    apiUrls = {
        "login": "/login",
        "currentAthlete": "/competition/{}/refereecurrentcompetitor",
        "refereeDecision": "/competition/{}/refereedecision"
    }

    def __init__(self, username, password, competitionId):
        self.login(username, password)
        self.competitionId = competitionId

    def login(self, username, password):
        response = requests.post(self._createUrl("login"), json = self._createLoginRequestBody(username, password))
        self.token = self._getResponseBody(response)["token"]

    def _createLoginRequestBody(self, username, password):
        return {"username": username, "password": password}

    def _createUrl(self, name):
        if name == "login":
            return self.baseUrl + self.apiUrls[name]
        elif name == "currentAthlete" or name == "refereeDecision":
            return self.baseUrl + self.apiUrls[name].format(self.competitionId)
        else:
            raise Exception("Unknown URL Name '{}'".format(name))

    def _getResponseBody(self, response):
        if response.ok:
            return response.json()
        else:
            raise Exception("Error Code {} occured with payload '{}'".format(response.status_code, response.text))
    
    def getCurrentAthlete(self):
        response = requests.get(self._createUrl("currentAthlete"), headers = self._createAuthorizationHeader())
        responseBody = self._getResponseBody(response)
        self.attemptLogId = responseBody["attemptLogId"]
        return responseBody

    def _createAuthorizationHeader(self):
        return {"Authorization": "Bearer {}".format(self.token)}

    def sendRefereeDecision(self, refereeType, refereeDecision):
        response = requests.post(self._createUrl("refereeDecision"), json = self._createRefereeDecisionRequestBody(refereeType, refereeDecision), headers = self._createAuthorizationHeader())
        return self._getResponseBody(response)

    def _createRefereeDecisionRequestBody(self, refereeType, refereeDecision):
        requestBody = {"attemptLogId": self.attemptLogId, "competitionId": self.competitionId, "refereeType": refereeType.value, "refereeId": 0}

        if refereeDecision == RefereeDecision.WHITE:
            requestBody["valid"] = True
            requestBody["notValidReason"] = None
        else:
            requestBody["valid"] = False
            requestBody["notValidReason"] = refereeDecision.value

        return requestBody