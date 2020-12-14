from threading import Timer

class CurrentAthleteRefresher:
    apiService = None
    pollingInterval = 5

    def __init__(self, apiService):
        self._startCurrentAthletePolling()
        self.apiService = apiService

    def _startCurrentAthletePolling(self):
        Timer(self.pollingInterval, self._pollCurrentAthlete).start()

    def _pollCurrentAthlete(self):
        print("Time Passed")
        #self.apiService.getCurrentAthlete()
        self._startCurrentAthletePolling()