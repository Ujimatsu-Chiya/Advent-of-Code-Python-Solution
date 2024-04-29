from collections import defaultdict, namedtuple

import requests

from utils import Solver

# https://dev.to/rpalo/aoc-day-20-a-regular-map-10ej
Leg = namedtuple('Leg', 'start begin end cont_start cont_end')


def mkleg(start, begin, end, cont_start=None, cont_end=None):
    return Leg(start, begin, end, cont_start, cont_end)


class Expedition:

    def __init__(self, regexp):
        self.regexp = regexp
        self.distances = defaultdict(lambda: float('inf'))
        self.doors = set()
        self.legs = {mkleg((1, 1), 0, len(self.regexp))}

    def explore(self):
        assert self.regexp[0] == '^' and self.regexp[-1] == '$'
        counter = 0
        while len(self.legs) > 0:
            next_leg = self.legs.pop()
            self.explore_leg(next_leg)
            counter += 1

    def explore_leg(self, current_leg):
        (x, y) = current_leg.start
        idx = current_leg.begin
        finish = False
        while idx < current_leg.end and not finish:
            old_pos = (x, y)
            current = self.regexp[idx]
            if current == '^':
                self.distances[(x, y)] = 0
            elif current == 'N':
                y -= 2
            elif current == 'E':
                x += 2
            elif current == 'S':
                y += 2
            elif current == 'W':
                x -= 2
            elif current == '$':
                pass
            elif current == '(':
                matching = self.find_matching(idx)
                options = self.find_options(idx, matching)
                for (option_begin, option_end) in options:
                    assert option_begin <= option_end
                    if option_begin < option_end:
                        leg = mkleg((x, y), option_begin, option_end, matching, current_leg.end)
                    else:
                        leg = mkleg((x, y), matching, current_leg.end)
                    self.legs.add(leg)
                finish = True
            elif current == ')':
                pass
            else:
                raise Exception('unexpected character ', current)
            self.distances[(x, y)] = min(1 + self.distances[old_pos], self.distances[(x, y)])
            idx += 1
        if current_leg.cont_start and current_leg.cont_start < current_leg.cont_end:
            leg = mkleg((x, y), current_leg.cont_start, current_leg.cont_end)
            self.legs.add(leg)

    def find_matching(self, idx):
        assert self.regexp[idx] == '('
        opened = 0
        while True:
            idx += 1
            current = self.regexp[idx]
            if current == '(':
                opened += 1
            elif current == ')' and opened == 0:
                return idx + 1
            elif current == ')':
                opened -= 1
            elif current == '^':
                raise Exception("regexp should be well constructed")

    def find_options(self, begin, end):
        assert self.regexp[begin] == '(' and self.regexp[end - 1] == ')'
        options = []
        opened = 0
        option_start = begin + 1
        for idx in range(begin + 1, end):
            current = self.regexp[idx]
            if current == '(':
                opened += 1
            elif current == ')':
                opened -= 1
            elif current == '|' and opened == 0:
                options.append((option_start, idx))
                option_start = idx + 1
            idx += 1
        options.append((option_start, end))
        return options


class Solver18D20(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/20/input'

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        expedition = Expedition(s)
        expedition.explore()
        return max(expedition.distances.values())

    def solve_part_2(self, src):
        s = self.parse(src)
        expedition = Expedition(s)
        expedition.explore()
        return sum(1 for v in expedition.distances.values() if v >= 1000)


if __name__ == "__main__":
    sol = Solver18D20()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D20.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
