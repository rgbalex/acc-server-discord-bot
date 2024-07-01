from cogs.models.Session import Session

class Event:
    def __init__(self):
        self.track = None
        self.eventType = None
        self.preRaceWaitingTimeSeconds = None
        self.postQualySeconds = None
        self.postRaceSeconds = None
        self.sessionOverTimeSeconds = None
        self.ambientTemp = None
        self.trackTemp = None
        self.cloudLevel : float = None
        self.rain : float = None
        self.weatherRandomness = None
        self.configVersion = None
        self.sessions = []

    def add_session(self, session: Session):
        self.sessions.append(session)