from utils import Solver, get_data
from tools import Point

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
order = "RDLU"


class Solver2023Day18(Solver):
    YEAR = 2023
    DAY = 18

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            dir, l, s = s.split()
            self.ops.append((dir, int(l), s[2:2 + 6]))

    def _solve(self, ls):
        x, y = 0, 0
        lt = [Point(x, y)]
        ans = premier = 0
        for dir, d in ls:
            x += dirs[dir][0] * d
            y += dirs[dir][1] * d
            premier += d
            lt.append(Point(x, y))
        n = len(lt)
        for i in range(n - 1):
            ans += lt[i] ^ lt[i + 1]
        return abs(ans) // 2 + premier // 2 + 1

    def solve_part_1(self):
        lt = [(dir, l) for dir, l, _ in self.ops]
        return self._solve(lt)

    def solve_part_2(self):
        lt = [(order[int(col[-1])], int(col[:5], 16)) for _, _, col in self.ops]
        return self._solve(lt)


if __name__ == "__main__":
    src = get_data(Solver2023Day18.YEAR, Solver2023Day18.DAY)
    sol = Solver2023Day18(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
