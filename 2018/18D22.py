import collections
import functools
import re

import requests

from utils import Solver

ROCKY, WET, NARROW = range(3)
CLIMBING_GEAR, TORCH, NEITHER = range(3)
COMPATIBILITY = {ROCKY: {CLIMBING_GEAR, TORCH},
                 WET: {CLIMBING_GEAR, NEITHER},
                 NARROW: {TORCH, NEITHER}}

State = collections.namedtuple('State', 'region equipment')


class Cave:
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target

    @functools.lru_cache(maxsize=None)
    def geologic_index(self, region, depth, target):
        x, y = region
        if region == (0, 0) or region == target:
            return 0
        elif y == 0:
            return x * 16807
        elif x == 0:
            return y * 48271
        else:
            return self.erosion_level((x - 1, y), depth, target) * self.erosion_level((x, y - 1), depth, target)

    def erosion_level(self, region, depth, target):
        return (self.geologic_index(region, depth, target) + depth) % 20183

    def cal_type(self, region, depth, target):
        return self.erosion_level(region, depth, target) % 3

    def type_(self, region):
        return self.cal_type(region, self.depth, self.target)

    def explore(self):
        fscore = collections.defaultdict(lambda: float('inf'))
        gscore = {}
        start = State(region=(0, 0), equipment=TORCH)

        gscore[start] = 0
        fscore[start] = self.heuristic(start)

        open_states = {start}
        closed_states = set()

        while True:
            current_state = min(open_states, key=lambda s: fscore[s])
            open_states.remove(current_state)

            if current_state.region == self.target and current_state.equipment == TORCH:
                return gscore[current_state]

            closed_states.add(current_state)

            for next_state, distance in self.neighborhood(current_state):

                if next_state in closed_states:
                    continue

                tentative_gscore = gscore[current_state] + distance

                if next_state not in open_states:
                    open_states.add(next_state)
                elif tentative_gscore > gscore[next_state]:
                    continue

                gscore[next_state] = tentative_gscore
                fscore[next_state] = tentative_gscore + self.heuristic(next_state)

    def heuristic(self, state):
        return abs(self.target[0] - state.region[0]) + abs(self.target[1] - state.region[1])

    def adjacent(self, region):
        x, y = region
        moves = []
        if x > 0:
            moves.append((x - 1, y))
        if y > 0:
            moves.append((x, y - 1))
        return moves + [(x + 1, y), (x, y + 1)]

    def neighborhood(self, current):
        next_states_and_distances = []
        for next_region in self.adjacent(current.region):
            if current.equipment in COMPATIBILITY[self.type_(next_region)]:
                next_states_and_distances.append((State(region=next_region, equipment=current.equipment), 1))
        for equipment in [CLIMBING_GEAR, TORCH, NEITHER]:
            if equipment != current.equipment and equipment in COMPATIBILITY[self.type_(current.region)]:
                next_states_and_distances.append((State(region=current.region, equipment=equipment), 7))
        return next_states_and_distances


class Solver18D22(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/22/input'

    def parse(self, src):
        pat = re.compile(r"(\d+)")
        a = list(map(int, pat.findall(src.strip())))
        return a

    def solve_part_1(self, src):
        dep, n, m = self.parse(src)
        cave = Cave(dep, (n, m))
        return sum(cave.cal_type((i, j), dep, (n, m)) for i in range(n + 1) for j in range(m + 1))

    def solve_part_2(self, src):
        dep, n, m = self.parse(src)
        cave = Cave(dep, (n, m))
        return cave.explore()


if __name__ == "__main__":
    sol = Solver18D22()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D22.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
