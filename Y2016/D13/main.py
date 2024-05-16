from queue import Queue

from utils import Solver, get_data


class Solver2016Day13(Solver):
    YEAR = 2016
    DAY = 13

    def __init__(self, src):
        self.w = int(src.strip())
        self.ans1 = self.ans2 = None

    def _gen(self, x, y, w):
        return (x * x + 3 * x + 2 * x * y + y + y * y + w).bit_count() & 1

    def run(self):
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ty, tx = 31, 39
        mp = {(1, 1): 0}
        q = Queue()
        q.put((1, 1))
        M = 50
        while q.qsize() > 0:
            nx, ny = q.get()
            if nx == tx and ny == ty:
                self.ans1 = mp[nx, ny]
            if self.ans1 is not None and mp[nx, ny] >= M:
                break
            for dx, dy in dirs:
                x, y = nx + dx, ny + dy
                if x >= 0 and y >= 0 and self._gen(y, x, self.w) == 0 and (x, y) not in mp.keys():
                    mp[x, y] = mp[nx, ny] + 1
                    q.put((x, y))
        self.ans2 = len([v for v in mp.values() if v <= M])

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day13.YEAR, Solver2016Day13.DAY)
    sol = Solver2016Day13(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
