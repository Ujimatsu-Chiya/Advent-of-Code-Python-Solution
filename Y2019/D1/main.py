from utils import Solver, get_data


class Solver2019Day1(Solver):
    YEAR = 2019
    DAY = 1

    def __init__(self, src):
        self.a = list(map(int, src.strip().split('\n')))

    def solve_part_1(self):
        return sum(x // 3 - 2 for x in self.a)

    def solve_part_2(self):

        def cal(x):
            return 0 if x <= 0 else x + cal(x // 3 - 2)

        return sum(cal(x) - x for x in self.a)


if __name__ == "__main__":
    src = get_data(Solver2019Day1.YEAR, Solver2019Day1.DAY)
    sol = Solver2019Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
