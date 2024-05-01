from utils import Solver, get_data


class Solver2018Day8(Solver):
    YEAR = 2018
    DAY = 8

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        a = self.parse(src)

        def dfs(i):
            ans = 0
            child = a[i]
            meta = a[i + 1]
            p = i + 2
            for _ in range(child):
                ans_t, cnt_t = dfs(p)
                p += cnt_t
                ans += ans_t
            ans += sum(a[p:p + meta])
            p += meta
            return ans, p - i

        return dfs(0)[0]

    def solve_part_2(self, src):
        a = self.parse(src)

        def dfs(i):
            child = a[i]
            meta = a[i + 1]
            ls = []
            p = i + 2
            for _ in range(child):
                val_t, cnt_t = dfs(p)
                p += cnt_t
                ls.append(val_t)
            if child == 0:
                val = sum(a[p:p + meta])
            else:
                val = sum(ls[i-1] for i in a[p:p+meta] if 1 <= i <= len(ls))
            p += meta
            return val, p - i

        return dfs(0)[0]


if __name__ == "__main__":
    sol = Solver2018Day8()
    src = get_data(Solver2018Day8.YEAR, Solver2018Day8.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
