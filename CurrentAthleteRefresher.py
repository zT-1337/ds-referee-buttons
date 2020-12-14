from threading import Timer
from ApiService import ApiService

class CurrentAthleteRefresher:
    apiService = None
    pollingInterval = 5

    def __init__(self, apiService: ApiService):
        self._startCurrentAthletePolling()
        self.apiService = apiService

    def _startCurrentAthletePolling(self):
        Timer(self.pollingInterval, self._pollCurrentAthlete).start()

    def _pollCurrentAthlete(self):
        print("Time Passed")
        #self.apiService.getCurrentAthlete()
        self._startCurrentAthletePolling()