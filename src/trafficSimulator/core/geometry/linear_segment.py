from .segment import Segment


class LinearSegment(Segment):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        super().__init__([start, end])

    def compute_x(self, t):
        return (1 - t) * self.start[0] + t * self.end[0]

    def compute_y(self, t):
        return (1 - t) * self.start[1] + t * self.end[1]

    def compute_dx(self, t):
        return self.end[0] - self.start[0]

    def compute_dy(self, t):
        return self.end[1] - self.start[1]
