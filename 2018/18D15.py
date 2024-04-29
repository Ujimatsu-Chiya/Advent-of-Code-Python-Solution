import collections
import enum
from dataclasses import dataclass
from itertools import count
from typing import NamedTuple

import requests

from utils import Solver


class Pt(NamedTuple('Pt', [('x', int), ('y', int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)

    @property
    def nb4(self):
        return [self + d for d in [Pt(0, 1), Pt(1, 0), Pt(0, -1), Pt(-1, 0)]]


class Team(enum.Enum):
    ELF = enum.auto()
    GOBLIN = enum.auto()


@dataclass
class Unit:
    team: Team
    position: Pt
    hp: int = 200
    alive: bool = True
    power: int = 3


class ElfDied(Exception):
    pass


class Grid(dict):
    def __init__(self, lines, power=3):
        super().__init__()

        self.units = []

        for i, line in enumerate(lines):
            for j, el in enumerate(line):
                self[Pt(i, j)] = el == '#'

                if el in 'EG':
                    self.units.append(Unit(
                        team={'E': Team.ELF, 'G': Team.GOBLIN}[el],
                        position=Pt(i, j),
                        power={'E': power, 'G': 3}[el]
                    ))

    def play(self, elf_death=False):
        rounds = 0
        while True:
            if self.round(elf_death=elf_death):
                break
            rounds += 1
        return rounds * sum(unit.hp for unit in self.units if unit.alive)

    def round(self, elf_death=False):
        for unit in sorted(self.units, key=lambda unit: unit.position):
            if unit.alive:
                if self.move(unit, elf_death=elf_death):
                    return True

    def move(self, unit, elf_death=False):
        targets = [target for target in self.units if unit.team != target.team and target.alive]
        occupied = set(u2.position for u2 in self.units if u2.alive and unit != u2)

        if not targets:
            return True

        in_range = set(pt for target in targets for pt in target.position.nb4 if not self[pt] and pt not in occupied)

        if not unit.position in in_range:
            move = self.find_move(unit.position, in_range)

            if move:
                unit.position = move

        opponents = [target for target in targets if target.position in unit.position.nb4]

        if opponents:
            target = min(opponents, key=lambda unit: (unit.hp, unit.position))

            target.hp -= unit.power

            if target.hp <= 0:
                target.alive = False
                if elf_death and target.team == Team.ELF:
                    raise ElfDied()

    def find_move(self, position, targets):
        visiting = collections.deque([(position, 0)])
        meta = {position: (0, None)}
        seen = set()
        occupied = {unit.position for unit in self.units if unit.alive}

        while visiting:
            pos, dist = visiting.popleft()
            for nb in pos.nb4:
                if self[nb] or nb in occupied:
                    continue
                if nb not in meta or meta[nb] > (dist + 1, pos):
                    meta[nb] = (dist + 1, pos)
                if nb in seen:
                    continue
                if not any(nb == visit[0] for visit in visiting):
                    visiting.append((nb, dist + 1))
            seen.add(pos)

        try:
            min_dist, closest = min((dist, pos) for pos, (dist, parent) in meta.items() if pos in targets)
        except ValueError:
            return

        while meta[closest][0] > 1:
            closest = meta[closest][1]

        return closest


class Solver18D15(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/15/input'

    def parse(self, src):
        return src.strip().split()

    def solve_part_1(self, src):
        ls = self.parse(src)
        return Grid(ls).play()

    def solve_part_2(self, src):
        ls = self.parse(src)
        for power in count(4):
            try:
                outcome = Grid(ls, power).play(elf_death=True)
            except ElfDied:
                continue
            else:
                return outcome


if __name__ == "__main__":
    sol = Solver18D15()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D15.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
