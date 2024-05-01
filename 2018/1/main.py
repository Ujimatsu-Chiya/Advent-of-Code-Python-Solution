from utils import Solver, get_data


class Solver2018Day1(Solver):
    YEAR = 2018
    DAY = 1

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        return sum(self.parse(src))

    def solve_part_2(self, src):
        a = self.parse(src)
        st = set()
        s = 0
        while True:
            for x in a:
                s += x
                if s in st:
                    return s
                st.add(s)


if __name__ == "__main__":
    sol = Solver2018Day1()
    src = get_data(Solver2018Day1.YEAR, Solver2018Day1.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
