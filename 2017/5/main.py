from utils import Solver, get_data


class Solver2017Day5(Solver):
    YEAR = 2017
    DAY = 5

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        a = self.parse(src)
        p = 0
        cnt = 0
        while 0 <= p < len(a):
            x = a[p]
            a[p] += 1
            p += x
            cnt += 1
        return cnt

    def solve_part_2(self, src):
        a = self.parse(src)
        p = 0
        cnt = 0
        while 0 <= p < len(a):
            x = a[p]
            a[p] = a[p] - 1 if a[p] >= 3 else a[p] + 1
            p += x
            cnt += 1
        return cnt

if __name__ == "__main__":
    sol = Solver2017Day5()
    src = get_data(Solver2017Day5.YEAR, Solver2017Day5.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
