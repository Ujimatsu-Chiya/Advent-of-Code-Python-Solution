from utils import Solver, get_data


class Solver2018Day8(Solver):
    YEAR = 2018
    DAY = 8

    def __init__(self, src):
        self.a = list(map(int, src.strip().split()))
        self.ans1 = self.ans2 = None

    def run(self):
        def dfs(i):
            ans = 0
            child = self.a[i]
            meta = self.a[i + 1]
            ls = []
            p = i + 2
            for _ in range(child):
                ans1_t, val_t, cnt_t = dfs(p)
                p += cnt_t
                ans += ans1_t
                ls.append(val_t)
            if child == 0:
                val = sum(self.a[p:p + meta])
            else:
                val = sum(ls[i - 1] for i in self.a[p:p + meta] if 1 <= i <= len(ls))
            ans += sum(self.a[p:p + meta])
            p += meta
            return ans, val, p - i
        self.ans1, self.ans2, _ = dfs(0)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day8.YEAR, Solver2018Day8.DAY)
    sol = Solver2018Day8(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
