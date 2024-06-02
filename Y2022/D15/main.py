import re

from utils import Solver, get_data


class Solver2022Day15(Solver):
    YEAR = 2022
    DAY = 15

    def __init__(self, src):
        pat = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
        self.queries = [list(map(int, v)) for v in pat.findall(src.strip())]

    def solve_part_1(self):
        Y = 2000000
        ls = []
        beacons = {(bx, by) for _, _, bx, by in self.queries}
        for sx, sy, bx, by in self.queries:
            d = abs(sx - bx) + abs(sy - by)
            if abs(sy - Y) <= d:
                dx = d - abs(sy - Y)
                ls.append((sx - dx, sx + dx))
        ls.sort()
        seg = []
        for l, r in ls:
            if len(seg) == 0 or l > seg[-1][1] + 1:
                seg.append([l, r])
            else:
                seg[-1][1] = max(seg[-1][1], r)
        cnt = sum(-1 for x, y in beacons if y == Y)
        for l, r in seg:
            cnt += r - l + 1
        return cnt

    def solve_part_2(self):
        M = 4000000
        vals = [[sx, sy, abs(sx - bx) + abs(sy - by)] for sx, sy, bx, by in self.queries]
        ka, kb = set(), set()
        for x, y, r in vals:
            ka |= {y - x + r + 1, y - x - r - 1}
            kb |= {x + y + r + 1, x + y - r - 1}
        for a in ka:
            for b in kb:
                px,py=(b-a)//2,(b+a)//2
                if 0 <= px <= M and 0 <= py <= M and all(abs(px-x)+abs(py-y) > r for x,y,r in vals ):
                    return M * px + py

if __name__ == "__main__":
    src = get_data(Solver2022Day15.YEAR, Solver2022Day15.DAY)
    sol = Solver2022Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
