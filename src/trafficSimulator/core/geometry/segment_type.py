from enum import Enum, auto


class SegmentType(Enum):
    LINEAR = auto()
    QUADRATIC_BEZIER = auto()
    CUBIC_BEZIER = auto()
