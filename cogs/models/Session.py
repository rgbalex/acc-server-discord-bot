import json, enum


class SessionType(enum.Enum):
    PRACTICE = "P"
    QUALIFYING = "Q"
    RACE = "R"
    UNDEFINED = "U"


class Session:
    def __init__(self):
        self.hourOfDay = None
        self.dayOfWeekend = None
        self.timeMultiplier = None
        self.sessionType = SessionType.UNDEFINED.value
        self.sessionDurationMinutes = None
