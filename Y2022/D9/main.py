from utils import Solver, get_data
from tools import sgn


class Solver2022Day9(Solver):
    YEAR = 2022
    DAY = 9

    def __init__(self, src):
        self.ops = [(s[0], int(s[2:])) for s in src.strip().split('\n')]

    def _run(self, M):
        dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
        st = set()
        snaps = [[0, 0] for _ in range(M + 1)]
        for ch, d in self.ops:
            for _ in range(d):
                snaps[0][0] += dirs[ch][0]
                snaps[0][1] += dirs[ch][1]
                for i in range(1, len(snaps)):
                    dx, dy = snaps[i - 1][0] - snaps[i][0], snaps[i - 1][1] - snaps[i][1]
                    if max(abs(dx), abs(dy)) > 1:
                        snaps[i][0] += sgn(dx)
                        snaps[i][1] += sgn(dy)
                st.add(tuple(snaps[-1]))
        return len(st)

    def solve_part_1(self):
        return self._run(1)

    def solve_part_2(self):
        return self._run(9)


if __name__ == "__main__":
    src = get_data(Solver2022Day9.YEAR, Solver2022Day9.DAY)
    sol = Solver2022Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
