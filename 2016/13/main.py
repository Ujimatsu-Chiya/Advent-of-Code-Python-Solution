from queue import Queue

from utils import Solver, get_data


class Solver2016Day13(Solver):
    YEAR = 2016
    DAY = 13
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def parse(self, src):
        return int(src.strip())

    def _gen(self, x, y, w):
        return (x * x + 3 * x + 2 * x * y + y + y * y + w).bit_count() & 1

    def solve_part_1(self, src):
        w = self.parse(src)
        ty, tx = 31, 39
        mp = {(1, 1): 0}
        q = Queue()
        q.put((1, 1))
        while q.qsize() > 0:
            nx, ny = q.get()
            if nx == tx and ny == ty:
                ans = mp[nx, ny]
                break
            for dx, dy in Solver2016Day13.dirs:
                x, y = nx + dx, ny + dy
                if x >= 0 and y >= 0 and self._gen(y, x, w) == 0 and (x, y) not in mp.keys():
                    mp[x, y] = mp[nx, ny] + 1
                    q.put((x, y))
        return ans

    def solve_part_2(self, src):
        w = self.parse(src)
        M = 50
        mp = {(1, 1): 0}
        q = Queue()
        q.put((1, 1))
        while q.qsize() > 0:
            nx, ny = q.get()
            if mp[nx,ny] == M:
                break
            for dx, dy in Solver2016Day13.dirs:
                x, y = nx + dx, ny + dy
                if x >= 0 and y >= 0 and self._gen(y, x, w) == 0 and (x, y) not in mp.keys():
                    mp[x, y] = mp[nx, ny] + 1
                    q.put((x, y))
        return len(mp)


if __name__ == "__main__":
    sol = Solver2016Day13()
    src = get_data(Solver2016Day13.YEAR, Solver2016Day13.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
