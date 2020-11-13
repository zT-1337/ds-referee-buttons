import requests
from enum import Enum, auto

class RefereeDecision(Enum):
    WHITE = auto()
    RED = auto()
    BLUE = auto()
    YELLOW = auto()


def login(username, password):
    pass

def getCurrentAthlete(competitionId):
    pass

def sendRefereeDecision(competitionId, attemptLogId, refereeType, refereeDecision):
    pass