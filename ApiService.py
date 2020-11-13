import requests
from enum import Enum, auto

class RefereeDecision(Enum):
    WHITE = auto()
    RED = auto()
    BLUE = auto()
    YELLOW = auto()

class RefereeType(Enum):
    Main = auto()
    LEFT = auto()
    RIGHT = auto()

def login(username, password):
    pass

def getCurrentAthlete(competitionId):
    response = requests.post("https://heavyplates.com/api/competition/{}/refereecurrentcompetitor".format(competitionId))
    
    if response.ok:
        return response.json()
    
    raise Exception("Error Code {} occured with payload '{}'".format(response.status_code, response.text))

def sendRefereeDecision(competitionId, attemptLogId, refereeType, refereeDecision):
    pass