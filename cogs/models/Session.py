import enum


class SessionType(enum.Enum):
    PRACTICE = "P"
    QUALIFYING = "Q"
    RACE = "R"
    UNDEFINED = "U"


class Session:
    def __init__(self):
        self.hourOfDay = 17
        self.dayOfWeekend = 1
        self.timeMultiplier = 1
        self.sessionType = SessionType.PRACTICE
        self.sessionDurationMinutes = 30

    def to_json(self):
        return {
            "hourOfDay": self.hourOfDay,
            "dayOfWeekend": self.dayOfWeekend,
            "timeMultiplier": self.timeMultiplier,
            "sessionType": self.sessionType.value,
            "sessionDurationMinutes": self.sessionDurationMinutes,
        }
