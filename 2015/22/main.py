import re
from math import inf

from utils import Solver, get_data


class Solver2015Day22(Solver):
    YEAR = 2015
    DAY = 22

    def parse(self, src):
        hit_points = int(re.search(r"Hit Points:\s*(\d+)", src.strip()).group(1))
        damage = int(re.search(r"Damage:\s*(\d+)", src.strip()).group(1))
        return hit_points, damage

    def solve_part_1(self, src):
        ans = inf
        hp2, damage2 = self.parse(src)
        hp1 = 50
        mana = 500

        def dfs(who, hp1, hp2, shield_turn, poison_turn, recharge_turn, mana, cost):
            nonlocal ans, damage2
            if shield_turn > 0:
                armor1 = 7
                shield_turn -= 1
            else:
                armor1 = 0
            if poison_turn > 0:
                hp2 -= 3
                poison_turn -= 1
            if recharge_turn > 0:
                mana += 101
                recharge_turn -= 1
            if cost > ans:
                return
            if hp1 <= 0:
                return
            if hp2 <= 0:
                ans = min(ans, cost)
                return
            if who == 1:
                attack2 = max(1, damage2 - armor1)
                hp1 -= attack2
                dfs(0, hp1, hp2, shield_turn, poison_turn, recharge_turn, mana, cost)
            else:
                if mana >= 53:
                    dfs(1, hp1, hp2 - 4, shield_turn, poison_turn, recharge_turn, mana - 53, cost + 53)
                if mana >= 73:
                    dfs(1, hp1 + 2, hp2 - 2, shield_turn, poison_turn, recharge_turn, mana - 73, cost + 73)
                if mana >= 113 and shield_turn == 0:
                    dfs(1, hp1, hp2, 6, poison_turn, recharge_turn, mana - 113, cost + 113)
                if mana >= 173 and poison_turn == 0:
                    dfs(1, hp1, hp2, shield_turn, 6, recharge_turn, mana - 173, cost + 173)
                if mana >= 229 and recharge_turn == 0:
                    dfs(1, hp1, hp2, shield_turn, poison_turn, 5, mana - 229, cost + 229)

        dfs(0, hp1, hp2, 0, 0, 0, mana, 0)
        return ans

    def solve_part_2(self, src):
        ans = inf
        hp2, damage2 = self.parse(src)
        hp1 = 50
        mana = 500

        def dfs(who, hp1, hp2, shield_turn, poison_turn, recharge_turn, mana, cost):
            nonlocal ans, damage2
            if who == 0:
                hp1 -= 1
            if shield_turn > 0:
                armor1 = 7
                shield_turn -= 1
            else:
                armor1 = 0
            if poison_turn > 0:
                hp2 -= 3
                poison_turn -= 1
            if recharge_turn > 0:
                mana += 101
                recharge_turn -= 1
            if cost > ans:
                return
            if hp1 <= 0:
                return
            if hp2 <= 0:
                ans = min(ans, cost)
                return
            if who == 1:
                attack2 = max(1, damage2 - armor1)
                hp1 -= attack2
                dfs(0, hp1, hp2, shield_turn, poison_turn, recharge_turn, mana, cost)
            else:
                if mana >= 53:
                    dfs(1, hp1, hp2 - 4, shield_turn, poison_turn, recharge_turn, mana - 53, cost + 53)
                if mana >= 73:
                    dfs(1, hp1 + 2, hp2 - 2, shield_turn, poison_turn, recharge_turn, mana - 73, cost + 73)
                if mana >= 113 and shield_turn == 0:
                    dfs(1, hp1, hp2, 6, poison_turn, recharge_turn, mana - 113, cost + 113)
                if mana >= 173 and poison_turn == 0:
                    dfs(1, hp1, hp2, shield_turn, 6, recharge_turn, mana - 173, cost + 173)
                if mana >= 229 and recharge_turn == 0:
                    dfs(1, hp1, hp2, shield_turn, poison_turn, 5, mana - 229, cost + 229)

        dfs(0, hp1, hp2, 0, 0, 0, mana, 0)
        return ans


if __name__ == "__main__":
    sol = Solver2015Day22()
    src = get_data(Solver2015Day22.YEAR, Solver2015Day22.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
