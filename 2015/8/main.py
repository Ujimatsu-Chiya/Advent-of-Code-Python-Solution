from utils import Solver, get_data


class Solver2015Day8(Solver):
    YEAR = 2015
    DAY = 8

    def parse(self, src):
        return src.strip().split('\n')

    def solve_part_1(self, src):
        ls = self.parse(src)
        ans = 0
        for s in ls:
            ans += len(s) - len(eval(s))
        return ans

    def solve_part_2(self, src):
        ls = self.parse(src)
        ans = 0
        lt = str(ls).strip('[]').replace(r'"', r'\"').split(', ')
        for s, t in zip(ls, lt):
            ans += len(t) - len(s)
        return ans


if __name__ == "__main__":
    sol = Solver2015Day8()
    src = get_data(Solver2015Day8.YEAR, Solver2015Day8.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
