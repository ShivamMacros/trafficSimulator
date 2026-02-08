from .segment_factory_interface import ISegmentFactory
from .segment import Segment
from .linear_segment import LinearSegment
from .quadratic_curve import QuadraticCurve
from .cubic_curve import CubicCurve
from .segment_type import SegmentType


class SegmentFactory(ISegmentFactory):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_linear(self, start: tuple, end: tuple) -> Segment:
        return LinearSegment(start, end)

    def create_quadratic_bezier(self, start: tuple, control: tuple, end: tuple) -> Segment:
        return QuadraticCurve(start, control, end)

    def create_cubic_bezier(self, start: tuple, control_1: tuple, control_2: tuple, end: tuple) -> Segment:
        return CubicCurve(start, control_1, control_2, end)

    def create(self, segment_type: SegmentType, *args) -> Segment:
        creators = {
            SegmentType.LINEAR: self.create_linear,
            SegmentType.QUADRATIC_BEZIER: self.create_quadratic_bezier,
            SegmentType.CUBIC_BEZIER: self.create_cubic_bezier,
        }
        creator = creators.get(segment_type)
        if creator is None:
            raise ValueError(f"Unknown segment type: {segment_type}")
        return creator(*args)
