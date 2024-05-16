from utils import Solver, get_data


class Solver2018Day1(Solver):
    YEAR = 2018
    DAY = 1

    def __init__(self, src):
        self.a= list(map(int, src.strip().split()))

    def solve_part_1(self):
        return sum(self.a)

    def solve_part_2(self):
        st = set()
        s = 0
        while True:
            for x in self.a:
                s += x
                if s in st:
                    return s
                st.add(s)


if __name__ == "__main__":
    src = get_data(Solver2018Day1.YEAR, Solver2018Day1.DAY)
    sol = Solver2018Day1(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
