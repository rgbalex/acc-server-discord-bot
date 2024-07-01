from cogs.models.Session import Session


class Event:
    def __init__(self):
        self.track = "barcelona"
        self.eventType = "E_6h"
        self.preRaceWaitingTimeSeconds = 80
        self.postQualySeconds = 15
        self.postRaceSeconds = 30
        self.sessionOverTimeSeconds = 120
        self.ambientTemp = 26
        self.trackTemp = 30
        self.cloudLevel: float = 0.30000001192092898
        self.rain: float = 0.0
        self.weatherRandomness = 1
        self.sessions = []
        self.configVersion = 1

    def add_session(self, session: Session):
        self.sessions.append(session)
