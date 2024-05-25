import re
from collections import defaultdict

from utils import Solver, get_data


class Solver2021Day5(Solver):
    YEAR = 2021
    DAY = 5

    def __init__(self, src):
        pat = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
        self.seg_list = [sorted([(int(v[0]), int(v[1])), (int(v[2]), int(v[3]))]) for v in pat.findall(src.strip())]
        self.ans1 = self.ans2 = None

    def run(self):
        mp = defaultdict(int)
        mq = defaultdict(int)
        for p0, p1 in self.seg_list:
            k = max(abs(p1[0] - p0[0]), abs(p1[1] - p0[1]))
            dx, dy = (p1[0] - p0[0]) // k, (p1[1] - p0[1]) // k
            for i in range(k+1):
                x, y = p0[0] + dx * i, p0[1] + dy * i
                mq[x, y] += 1
                if dx == 0 or dy == 0:
                    mp[x, y] += 1
        self.ans1 = sum(1 for v in mp.values() if v > 1)
        self.ans2 = sum(1 for v in mq.values() if v > 1)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day5.YEAR, Solver2021Day5.DAY)
    sol = Solver2021Day5(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
