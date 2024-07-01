from enum import Enum


class ListableEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class TrackType(ListableEnum):
    BARCELONA = "barcelona"
    BRANDS_HATCH = "brands_hatch"
    COTA = "cota"
    DONINGTON = "donington"
    HUNGARORING = "hungaroring"
    IMOLA = "imola"
    INDIANAPOLIS = "indianapolis"
    KYALAMI = "kyalami"
    LAGUNA_SECA = "laguna_seca"
    MISANO = "misano"
    MONZA = "monza"
    MOUNT_PANORAMA = "mount_panorama"
    NURBURGRING = "nurburgring"
    NURBURGRING_24H = "nurburgring_24h"
    OULTON_PARK = "oulton_park"
    PAUL_RICARD = "paul_ricard"
    RED_BULL_RING = "red_bull_ring"
    SILVERSTONE = "silverstone"
    SNETTERTON = "snetterton"
    SPA = "spa"
    SUZUKA = "suzuka"
    VALENCIA = "valencia"
    WATKINS_GLEN = "watkins_glen"
    ZANDVOORT = "zandvoort"
    ZOLDER = "zolder"
