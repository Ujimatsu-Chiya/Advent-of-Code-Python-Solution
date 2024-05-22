from collections import defaultdict

from utils import Solver, get_data


class Solver2020Day15(Solver):
    YEAR = 2020
    DAY = 15

    def __init__(self, src):
        self.a = list(map(int, src.strip().split(',')))

    def _run(self, a, M):
        mp = defaultdict(list)
        for i, x in enumerate(a):
            mp[x].append(i)
        x = a[-1]
        for i in range(len(a), M):
            if len(mp[x]) == 1:
                x = 0
            else:
                x = mp[x][-1] - mp[x][-2]
            mp[x].append(i)
        return x

    def solve_part_1(self):
        return self._run(self.a, 2020)

    def solve_part_2(self):
        return self._run(self.a, 30000000)


if __name__ == "__main__":
    src = get_data(Solver2020Day15.YEAR, Solver2020Day15.DAY)
    sol = Solver2020Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
