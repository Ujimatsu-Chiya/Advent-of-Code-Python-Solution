from utils import Solver, get_data


class Solver2019Day4(Solver):
    YEAR = 2019
    DAY = 4

    def __init__(self, src):
        self.l, self.r = map(int, src.strip().split('-'))

    def solve_part_1(self):
        return sum(1 for i in range(self.l, self.r + 1) if (lambda s:
            any(s[i] == s[i - 1] for i in range(1, len(s))) and all(s[i] >= s[i - 1] for i in range(1, len(s))))
                   (str(i)))

    def solve_part_2(self):
        return sum(1 for i in range(self.l, self.r + 1) if (lambda s:
            2 in map(s.count, s) and all(s[i] >= s[i - 1] for i in range(1, len(s))))
                   (str(i)))


if __name__ == "__main__":
    src = get_data(Solver2019Day4.YEAR, Solver2019Day4.DAY)
    sol = Solver2019Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
