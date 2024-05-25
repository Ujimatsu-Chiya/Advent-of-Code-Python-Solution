from collections import deque

from utils import Solver, get_data


class Solver2021Day6(Solver):
    YEAR = 2021
    DAY = 6

    def __init__(self, src):
        self.ls = [int(s) for s in src.strip().split(',')]

    def _run(self, T):
        M = 8
        q = deque([self.ls.count(i) for i in range(M + 1)])
        for _ in range(T):
            x = q.popleft()
            q.append(x)
            q[6] += x
        return sum(q)

    def solve_part_1(self):
        return self._run(80)

    def solve_part_2(self):
        return self._run(256)


if __name__ == "__main__":
    src = get_data(Solver2021Day6.YEAR, Solver2021Day6.DAY)
    sol = Solver2021Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
