from utils import Solver, get_data


class Solver2017Day1(Solver):
    YEAR = 2017
    DAY = 1

    def parse(self, src):
        return src.strip()

    def solve_part_1(self, src):
        s = self.parse(src)
        return sum(int(s[i]) for i in range(len(s)) if s[i] == s[(i + 1) % len(s)])

    def solve_part_2(self, src):
        s = self.parse(src)
        return sum(int(s[i]) * 2 for i in range(len(s) // 2) if s[i] == s[i+len(s) // 2])


if __name__ == "__main__":
    sol = Solver2017Day1()
    src = get_data(Solver2017Day1.YEAR, Solver2017Day1.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
