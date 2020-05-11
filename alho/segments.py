def find_position(segments, segment):
    last_index = len(segments) - 1

    if not len(segments):
        return 0

    if len(segments) == 1:
        if segments[0].b == segment.b:
            return None
        return 1 if segments[0].b < segment.b else 0

    if segments[0].b > segment.b:
        return 0

    for index in range(0, last_index):
        if segments[index].b == segment.b or segments[index + 1].b == segment.b:
            return None
        if segments[index].b < segment.b < segments[index + 1].b:
            return index + 1

    return last_index + 1


class Segment:
    def __init__(self, a, b):
        self.a = min(a, b)
        self.b = max(a, b)

    def __repr__(self):
        return f'{self.a} {self.b}'


class Segments:
    def __init__(self):
        self.segments = []
        self.dots = []

    def add(self, segment):
        index = find_position(self.segments, segment)
        if index == 0 or not index is None:
            self.segments[index:index] = [segment]

    def find_dots(self):
        while len(self.segments):
            if len(self.segments) == 1:
                self.dots.append(str(self.segments[0].b))
                self.segments = []
            else:
                amount_remove = 1
                while amount_remove < len(self.segments) and self.segments[amount_remove].a <= self.segments[0].b:
                    amount_remove += 1

                self.dots.append(str(self.segments[0].b))
                self.segments = self.segments[amount_remove:len(self.segments)]


segments = Segments()
amount_lines = int(input())
for _ in range(amount_lines):
    a, b = map(int, input().split(' '))
    segments.add(Segment(a, b))
print(segments.segments)
segments.find_dots()
print(len(segments.dots))
print(' '.join(segments.dots))
