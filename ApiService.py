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

def login(username, password):
    pass

def getCurrentAthlete(competitionId):
    response = requests.post("https://heavyplates.com/api/competition/{}/refereecurrentcompetitor".format(competitionId))
    return handleResponse(response)

def handleResponse(response):
    if response.ok:
        return response.json()

    raise Exception("Error Code {} occured with payload '{}'".format(response.status_code, response.text))

def sendRefereeDecision(competitionId, attemptLogId, refereeType, refereeDecision):
    requestBody = createRefereeDecisionRequestBody(competitionId, attemptLogId, refereeType, refereeDecision)
    response = requests.post("https://heavyplates.com/api/competition/{}/refereedecision".format(competitionId), requestBody)
    return handleResponse(response)

def createRefereeDecisionRequestBody(competitionId, attemptLogId, refereeType, refereeDecision):
    requestBody = {"attemptLogId": attemptLogId, "competitionId": competitionId, "refereeType": refereeType.value, "refereeId": 0}

    if refereeDecision == RefereeDecision.WHITE:
        requestBody["valid"] = True
        requestBody["notValidReason"] = None
    else:
        requestBody["valid"] = False
        requestBody["notValidReason"] = refereeDecision.value

    return requestBody