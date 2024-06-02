import re
from fractions import Fraction
from itertools import combinations

from sympy import Symbol, solve_poly_system

from utils import Solver, get_data


class Solver2023Day24(Solver):
    YEAR = 2023
    DAY = 24

    def __init__(self, src):
        pat = re.compile(r"(\d+),\s*(\d+),\s*(\d+)\s*@\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)")
        self.queries = [list(map(lambda x: int(x), vec)) for vec in pat.findall(src.strip())]

    def solve_part_1(self):
        # mn = 200000000000000
        # mx = 400000000000000
        # ans = 0
        # for p0, p1 in combinations(self.queries, 2):
        #     try:
        #         x, y, t0, t1 = Symbol('x'), Symbol('y'), Symbol('t0'), Symbol('t1')
        #         res = solve_poly_system([
        #             p0[0] + p0[3] * t0 - x,
        #             p1[0] + p1[3] * t1 - x,
        #             p0[1] + p0[4] * t0 - y,
        #             p1[1] + p1[4] * t1 - y,
        #         ], x, y, t0, t1)[0]
        #     except Exception:
        #         res = []
        #     if res:
        #         if mn <= res[0] <= mx and mn <= res[1] <= mx and res[2] >= 0 and res[3] >= 0:
        #             ans += 1
        #     print(ans)
        # return ans

        def solve(l0, l1):
            a, b, e = l0
            c, d, f = l1
            D = l0[0] * l1[1] - l0[1] * l1[0]
            if D == 0:
                return None, None
            Dx, Dy = e * d - b * f, a * f - e * c
            x, y = Dx / D, Dy / D
            return x, y

        mn = 200000000000000
        mx = 400000000000000
        ans = 0
        for p0, p1 in combinations(self.queries, 2):
            l0 = [p0[4], -p0[3], p0[4] * p0[0] - p0[3] * p0[1]]
            l1 = [p1[4], -p1[3], p1[4] * p1[0] - p1[3] * p1[1]]
            x, y = solve(l0, l1)
            if x is not None:
                t0 = next((new_pos - pre_pos) / v for new_pos, pre_pos, v in zip([x, y], p0[:2], p0[3:5]) if v != 0)
                t1 = next((new_pos - pre_pos) / v for new_pos, pre_pos, v in zip([x, y], p1[:2], p1[3:5]) if v != 0)
                if 0 <= t0 and 0 <= t1 and mn <= x <= mx and mn <= y <= mx:
                    ans += 1
        return ans

    def solve_part_2(self):
        x, y, z, dx, dy, dz = Symbol('x'), Symbol('y'), Symbol('z'), Symbol('dx'), Symbol('dy'), Symbol('dz')
        symbols = [x, y, z, dx, dy, dz]
        equations = []
        for i, p in enumerate(self.queries[:3]):
            t = Symbol('t{}'.format(i))
            equations += [
                p[0] + p[3] * t - (x + dx * t),
                p[1] + p[4] * t - (y + dy * t),
                p[2] + p[5] * t - (z + dz * t)
            ]
            symbols.append(t)
        res = solve_poly_system(equations, *symbols)[0]
        return int(sum(res[:3]))


if __name__ == "__main__":
    src = get_data(Solver2023Day24.YEAR, Solver2023Day24.DAY)
    sol = Solver2023Day24(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
