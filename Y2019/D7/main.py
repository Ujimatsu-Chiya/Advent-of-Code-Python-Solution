from itertools import permutations
from tools import IntCodeComputer
from utils import Solver, get_data


class Solver2019Day7(Solver):
    YEAR = 2019
    DAY = 7

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def _run(self, a):
        ans = -1
        for p in permutations(a):
            comp = [IntCodeComputer(self.ops, [p[i]]) for i in range(5)]
            comp[0].add_input(0)
            idx = 0
            last = -1
            while any(not com.halt for com in comp):
                last = comp[idx].get_output()
                idx = (idx + 1) % 5
                comp[idx].add_input(last)
            ans = max(ans, last)
        return ans

    def solve_part_1(self):
        return self._run(range(5))

    def solve_part_2(self):
        return self._run(range(5, 10))


if __name__ == "__main__":
    src = get_data(Solver2019Day7.YEAR, Solver2019Day7.DAY)
    sol = Solver2019Day7(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
