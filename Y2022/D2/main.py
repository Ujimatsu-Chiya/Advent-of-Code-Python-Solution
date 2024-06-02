from utils import Solver, get_data


class Solver2022Day2(Solver):
    YEAR = 2022
    DAY = 2

    def __init__(self, src):
        self.queries = [s.split() for s in src.strip().split('\n')]

    def solve_part_1(self):
        ans = 0
        for c1, c2 in self.queries:
            x = {'A': 0, 'B': 1, 'C': 2}[c1]
            y = {'X': 0, 'Y': 1, 'Z': 2}[c2]
            w = 3 if x == y else 6 if x == (y - 1) % 3 else 0
            ans += y + 1 + w
        return ans

    def solve_part_2(self):
        ans = 0
        for c1, c2 in self.queries:
            x = {'A': 0, 'B': 1, 'C': 2}[c1]
            v, w = {'X': (-1, 0), 'Y': (0, 3), 'Z': (1, 6)}[c2]
            y = (x + v) % 3
            ans += y + 1 + w
        return ans


if __name__ == "__main__":
    src = get_data(Solver2022Day2.YEAR, Solver2022Day2.DAY)
    sol = Solver2022Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
