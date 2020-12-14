from threading import Timer 

class CurrentAthleteRefresher:
    pollingTimer = None

    def __init__(self):
        self.pollingTimer = Timer(2, self._startAthletePolling)
        pass

    def _startAthletePolling(self):
        print("Time passed")