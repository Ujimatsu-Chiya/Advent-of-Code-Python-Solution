import re

from utils import Solver, get_data
from itertools import combinations


class Solver2015Day21(Solver):
    YEAR = 2015
    DAY = 21

    def __init__(self, src):
        self.hp2 = int(re.search(r"Hit Points:\s*(\d+)", src.strip()).group(1))
        self.damage2 = int(re.search(r"Damage:\s*(\d+)", src.strip()).group(1))
        self.armor2 = int(re.search(r"Armor:\s*(\d+)", src.strip()).group(1))
        self.ans1 = self.ans2 = None

    def run(self):
        weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
        armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
        rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]
        hp1 = 100
        armors += [[0, 0, 0]]
        rings += [[sum(v) for v in zip(*comb)] for comb in combinations(rings, 2)] + [[0, 0, 0]]
        hp2, damage2, armor2 = self.hp2, self.damage2, self.armor2
        self.ans1 = max(weapons + armors + rings)[0] * 3
        self.ans2 = -1
        for i in range(len(weapons)):
            for j in range(len(armors)):
                for k in range(len(rings)):
                    v = [weapons[i], armors[j], rings[k]]
                    cost, damage1, armor1 = [sum(v[i][j] for i in range(len(v))) for j in range(3)]
                    attack1 = max(damage1 - armor2, 1)
                    attack2 = max(damage2 - armor1, 1)
                    if (hp2 + attack1 - 1) // attack1 <= (hp1 + attack2 - 1) // attack2:
                        self.ans1 = min(self.ans1, cost)
                    else:
                        self.ans2 = max(self.ans2, cost)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2015Day21.YEAR, Solver2015Day21.DAY)
    sol = Solver2015Day21(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
