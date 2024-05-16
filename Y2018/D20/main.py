from collections import defaultdict
from typing import NamedTuple, Optional

from utils import Solver, get_data


class Seg(NamedTuple):
    start: tuple
    begin: int
    end: int
    cont_start: Optional[int] = None
    cont_end: Optional[int] = None


class Expedition:

    def __init__(self, s):
        self.s = s
        self.dis = defaultdict(lambda: float('inf'))
        self.dis[(1, 1)] = 0
        self.doors = set()
        self.segs = {Seg((1, 1), 1, len(self.s) - 1)}
        st = []
        self.data = dict()
        for i, ch in enumerate(s):
            if ch == '(':
                st.append([i, i])
                self.data[i] = [0, []]
            elif ch == ')':
                x, pre = st[-1]
                self.data[x][0] = i
                self.data[x][1].append([pre + 1, i])
                st.pop()
            elif ch == '|':
                x, pre = st[-1]
                self.data[x][1].append([pre + 1, i])
                st[-1][1] = i

    def explore(self):
        assert self.s[0] == '^' and self.s[-1] == '$'
        while len(self.segs) > 0:
            seg = self.segs.pop()
            self.explore_seg(seg)

    def explore_seg(self, seg):
        (x, y) = seg.start
        idx = seg.begin
        finish = False
        while idx < seg.end and not finish:
            old_pos = (x, y)
            ch = self.s[idx]
            if ch == 'N':
                y -= 2
            elif ch == 'E':
                x += 2
            elif ch == 'S':
                y += 2
            elif ch == 'W':
                x -= 2
            elif ch == '(':
                matching, options = self.data[idx]
                for option_begin, option_end in options:
                    if option_begin < option_end:
                        seg = Seg((x, y), option_begin, option_end, matching, seg.end)
                    else:
                        seg = Seg((x, y), matching, seg.end)
                    self.segs.add(seg)
                finish = True
            self.dis[(x, y)] = min(1 + self.dis[old_pos], self.dis[(x, y)])
            idx += 1
        if seg.cont_start and seg.cont_start < seg.cont_end:
            seg = Seg((x, y), seg.cont_start, seg.cont_end)
            self.segs.add(seg)


class Solver2018Day20(Solver):
    YEAR = 2018
    DAY = 20

    def __init__(self, src):
        self.s = src.strip()
        self.ans1 = self.ans2 = None

    def run(self):
        expedition = Expedition(self.s)
        expedition.explore()
        self.ans1 = max(expedition.dis.values())
        self.ans2 = sum(1 for v in expedition.dis.values() if v >= 1000)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day20.YEAR, Solver2018Day20.DAY)
    sol = Solver2018Day20(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
