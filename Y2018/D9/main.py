import re
from collections import deque

from utils import Solver, get_data


class Solver2018Day9(Solver):
    YEAR = 2018
    DAY = 9

    def __init__(self, src):
        self.n, self.m = map(int, re.findall(r'\d+', src.strip()))

    def _run(self, n, m):
        cnt = [0 for _ in range(n)]
        q = deque([0])

        for i in range(1, m + 1):
            if i % 23 == 0:
                q.rotate(7)
                cnt[i % n] += i + q.pop()
                q.rotate(-1)
            else:
                q.rotate(-1)
                q.append(i)

        return max(cnt)

    def solve_part_1(self):
        return self._run(self.n, self.m)

    def solve_part_2(self):
        return self._run(self.n, self.m * 100)


if __name__ == "__main__":
    src = get_data(Solver2018Day9.YEAR, Solver2018Day9.DAY)
    sol = Solver2018Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
