from collections import deque
from enum import Enum, auto
from dataclasses import dataclass
from itertools import count
from math import inf
from tools import Point
from utils import Solver, get_data


class Team(Enum):
    ELF = auto()
    GOBLIN = auto()


@dataclass
class Unit:
    team: Team
    pos: Point
    hp: int = 200
    alive: bool = True
    power: int = 3


class Grid:
    def __init__(self, mp, power=3):
        self.mp = {}
        self.units = []
        for i, line in enumerate(mp):
            for j, el in enumerate(line):
                self.mp[Point(i, j)] = el == '#'
                if el in 'EG':
                    self.units.append(Unit(
                        team={'E': Team.ELF, 'G': Team.GOBLIN}[el],
                        pos=Point(i, j),
                        power={'E': power, 'G': 3}[el]
                    ))

    def play(self, part2=False):
        for r in count():
            self.units = [unit for unit in self.units if unit.alive]
            if self.round(part2=part2):
                break
        return r * sum(unit.hp for unit in self.units if unit.alive)

    def round(self, part2=False):
        for unit in sorted(self.units, key=lambda unit: unit.pos):
            if unit.alive:
                if self.move(unit, part2=part2):
                    return True

    def move(self, unit: Unit, part2=False):
        targets = [target for target in self.units if unit.team != target.team and target.alive]
        occupied = set(u2.pos for u2 in self.units if u2.alive and unit is not u2)
        if not targets:
            return True

        in_range = set(p for target in targets for p in target.pos.neighbor4() if not self.mp[p] and p not in occupied)
        if not unit.pos in in_range:
            move = self.find_move(unit.pos, in_range)
            if move:
                unit.pos = move

        opponents = [target for target in targets if target.pos in unit.pos.neighbor4()]

        if opponents:
            target = min(opponents, key=lambda unit: (unit.hp, unit.pos))
            target.hp -= unit.power
            if target.hp <= 0:
                target.alive = False
                if part2 and target.team == Team.ELF:
                    raise AttributeError

    def find_move(self, pos, targets):
        q = deque([pos])
        data = {pos: (0, None)}
        occupied = {unit.pos for unit in self.units if unit.alive}
        while q:
            u = q.popleft()
            for v in u.neighbor4():
                if self.mp[v] or v in occupied:
                    continue
                if v not in data.keys():
                    q.append(v)
                data[v] = min(data.get(v, (inf,)), (data[u][0] + 1, u))
        tp = [(data[k][0], k) for k in data.keys() if k in targets]
        if tp:
            u = min(tp)[1]
            while data[u][0] > 1:
                u = data[u][1]
            return u


class Solver2018Day15(Solver):
    YEAR = 2018
    DAY = 15

    def __init__(self, src):
        self.ls = src.strip().split()

    def solve_part_1(self):
        return Grid(self.ls).play()

    def solve_part_2(self):
        for power in count(4):
            try:
                outcome = Grid(self.ls, power).play(part2=True)
            except AttributeError:
                continue
            else:
                return outcome


if __name__ == "__main__":
    src = get_data(Solver2018Day15.YEAR, Solver2018Day15.DAY)
    sol = Solver2018Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
