from threading import Timer

class CurrentAthleteRefresher:
    apiService = None
    pollingInterval = None

    def __init__(self, apiService, pollingInterval):
        self.apiService = apiService
        self.pollingInterval = pollingInterval
        self._startCurrentAthletePolling()
        

    def _startCurrentAthletePolling(self):
        Timer(self.pollingInterval, self._pollCurrentAthlete).start()

    def _pollCurrentAthlete(self):
        print("Time Passed")
        #self.apiService.getCurrentAthlete()
        self._startCurrentAthletePolling()