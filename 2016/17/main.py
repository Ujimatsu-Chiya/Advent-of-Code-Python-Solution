import hashlib
from queue import Queue

from utils import Solver, get_data


class Solver2016Day17(Solver):
    YEAR = 2016
    DAY = 17

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        start = self.parse(src)
        ok = "bcdef"
        dirs = [[-1, 0, 'U'], [1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R']]
        n = m = 4
        q = Queue()
        q.put((0, 0, start))
        while q.qsize() > 0:
            sx, sy, s = q.get()
            md5 = hashlib.md5(s.encode())
            t = md5.hexdigest()[:4]
            for i in range(4):
                if t[i] in ok:
                    dx, dy, ch = dirs[i]
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m:
                        if x == n - 1 and y == m - 1:
                            return (s + ch)[len(start):]
                        else:
                            q.put((sx + dx, sy + dy, s + ch))

    def solve_part_2(self, src):
        start = self.parse(src)
        ok = "bcdef"
        dirs = [[-1, 0, 'U'], [1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R']]
        n = m = 4
        q = Queue()
        q.put((0, 0, start))
        ans = 0
        while q.qsize() > 0:
            sx, sy, s = q.get()
            md5 = hashlib.md5(s.encode())
            t = md5.hexdigest()[:4]
            for i in range(4):
                if t[i] in ok:
                    dx, dy, ch = dirs[i]
                    x, y = sx + dx, sy + dy
                    if 0 <= x < n and 0 <= y < m:
                        if x == n - 1 and y == m - 1:
                            ans = max(ans, len(s) + 1 - len(start))
                        else:
                            q.put((sx + dx, sy + dy, s + ch))
        return ans

if __name__ == "__main__":
    sol = Solver2016Day17()
    src = get_data(Solver2016Day17.YEAR, Solver2016Day17.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))