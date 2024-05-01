import re

from utils import Solver, get_data


class Solver2015Day21(Solver):
    YEAR = 2015
    DAY = 21

    weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
    armor = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
    rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]

    def parse(self, src):
        hp = int(re.search(r"Hit Points:\s*(\d+)", src.strip()).group(1))
        damage = int(re.search(r"Damage:\s*(\d+)", src.strip()).group(1))
        armor = int(re.search(r"Armor:\s*(\d+)", src.strip()).group(1))
        return hp, damage, armor

    def solve_part_1(self, src):
        hp2, damage2, armor2 = self.parse(src)
        hp1 = 100
        weapons = Solver2015Day21.weapons
        armor = Solver2015Day21.armor + [[0, 0, 0]]
        rings = Solver2015Day21.rings + [[0, 0, 0]]
        for i in range(len(Solver2015Day21.rings)):
            for j in range(i):
                rings.append([rings[i][p] + rings[j][p] for p in range(3)])

        ans = max(weapons)[0] + max(armor)[0] + max(rings)[0]
        for i in range(len(weapons)):
            for j in range(len(armor)):
                for k in range(len(rings)):
                    v = [weapons[i], armor[j], rings[k]]
                    cost, damage1, armor1 = [sum(v[i][j] for i in range(len(v))) for j in range(3)]
                    attack1 = max(damage1 - armor2, 1)
                    attack2 = max(damage2 - armor1, 1)
                    if (hp2 + attack1 - 1) // attack1 <= (hp1 + attack2 - 1) // attack2:
                        ans = min(ans, cost)
        return ans

    def solve_part_2(self, src):
        hp2, damage2, armor2 = self.parse(src)
        hit_points1 = 100
        weapons = Solver2015Day21.weapons
        armor = Solver2015Day21.armor + [[0, 0, 0]]
        rings = Solver2015Day21.rings + [[0, 0, 0]]
        for i in range(len(Solver2015Day21.rings)):
            for j in range(i):
                rings.append([rings[i][p] + rings[j][p] for p in range(3)])

        ans = 0
        for i in range(len(weapons)):
            for j in range(len(armor)):
                for k in range(len(rings)):
                    v = [weapons[i], armor[j], rings[k]]
                    cost, damage1, armor1 = [sum(v[i][j] for i in range(len(v))) for j in range(3)]
                    attack1 = max(damage1 - armor2, 1)
                    attack2 = max(damage2 - armor1, 1)
                    if (hp2 + attack1 - 1) // attack1 > (hit_points1 + attack2 - 1) // attack2:
                        ans = max(ans, cost)
        return ans


if __name__ == "__main__":
    sol = Solver2015Day21()
    src = get_data(Solver2015Day21.YEAR, Solver2015Day21.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
