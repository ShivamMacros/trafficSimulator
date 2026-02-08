from abc import ABC, abstractmethod
from .segment import Segment


class ISegmentFactory(ABC):
    @abstractmethod
    def create_linear(self, start: tuple, end: tuple) -> Segment:
        pass

    @abstractmethod
    def create_quadratic_bezier(self, start: tuple, control: tuple, end: tuple) -> Segment:
        pass

    @abstractmethod
    def create_cubic_bezier(self, start: tuple, control_1: tuple, control_2: tuple, end: tuple) -> Segment:
        pass
