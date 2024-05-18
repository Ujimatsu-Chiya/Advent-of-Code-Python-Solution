from utils import Solver, get_data


class Solver2020Day5(Solver):
    YEAR = 2020
    DAY = 5

    def __init__(self, src):
        self.queries = src.strip().split()
        self.ans1 = self.ans2 = None

    def run(self):
        self.ans1 = 0
        ls = []
        for s in self.queries:
            t = s.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
            x = int(t, 2)
            self.ans1 = max(self.ans1, x)
            ls.append(x)
        s, mn, mx = sum(ls), min(ls), max(ls)
        self.ans2 = (mn + mx) * (mx - mn + 1) // 2 - s

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day5.YEAR, Solver2020Day5.DAY)
    sol = Solver2020Day5(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
