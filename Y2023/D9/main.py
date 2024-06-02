from utils import Solver, get_data


class Solver2023Day9(Solver):
    YEAR = 2023
    DAY = 9

    def __init__(self, src):
        self.ls = [list(map(int, t.split())) for t in src.strip().split('\n')]

    def solve_part_1(self):
        ans = 0
        for u in self.ls:
            now = [u]
            while True:
                v = []
                for i in range(len(now[-1]) - 1):
                    v.append(now[-1][i + 1] - now[-1][i])
                now.append(v)
                if v.count(0) == len(v):
                    break
            for i in range(len(now) - 1, 0, -1):
                now[i - 1].append(now[i - 1][-1] + now[i][-1])
            ans += now[0][-1]
        return ans

    def solve_part_2(self):
        ans = 0
        for u in self.ls:
            now = [list(reversed(u))]
            while True:
                v = []
                for i in range(len(now[-1]) - 1):
                    v.append(now[-1][i + 1] - now[-1][i])
                now.append(v)
                if v.count(0) == len(v):
                    break
            for i in range(len(now) - 1, 0, -1):
                now[i - 1].append(now[i - 1][-1] + now[i][-1])
            ans += now[0][-1]
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day9.YEAR, Solver2023Day9.DAY)
    sol = Solver2023Day9(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
