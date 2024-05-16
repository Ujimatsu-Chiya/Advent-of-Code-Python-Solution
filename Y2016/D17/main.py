import hashlib
from queue import Queue

from tools import md5_digest
from utils import Solver, get_data


class Solver2016Day17(Solver):
    YEAR = 2016
    DAY = 17

    def __init__(self, src):
        self.start = src.strip()
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans2 = 0
        ok = "bcdef"
        dirs = [[-1, 0, 'U'], [1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R']]
        n = m = 4
        q = Queue()
        q.put((0, 0, self.start))
        while q.qsize() > 0:
            sx, sy, s = q.get()
            t = md5_digest(s)
            for i in range(4):
                if t[i] in ok:
                    dx, dy, ch = dirs[i]
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m:
                        if x == n - 1 and y == m - 1:
                            if self.ans1 is None:
                                self.ans1 = (s + ch)[len(self.start):]
                            self.ans2 = max(self.ans2, len(s) + 1 - len(self.start))
                        else:
                            q.put((sx + dx, sy + dy, s + ch))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day17.YEAR, Solver2016Day17.DAY)
    sol = Solver2016Day17(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
