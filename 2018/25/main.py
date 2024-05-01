from utils import Solver, get_data


class Solver2018Day25(Solver):
    YEAR = 2018
    DAY = 25

    def parse(self, src):
        ls = []
        for s in src.strip().split():
            ls.append(list(map(int, s.split(','))))
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        n = len(ls)
        fa = list(range(n))

        def find(x):
            if fa[x] == x:
                return x
            else:
                fa[x] = find(fa[x])
            return fa[x]

        def merge(x, y):
            fa[find(x)] = find(y)

        for i in range(n):
            for j in range(i):
                s = sum(abs(ls[i][k] - ls[j][k]) for k in range(4))
                if s <= 3:
                    merge(i, j)
        ans = 0
        for i in range(n):
            if i == find(i):
                ans += 1
        return ans

    def solve_part_2(self, src):
        n = self.parse(src)


if __name__ == "__main__":
    sol = Solver2018Day25()
    src = get_data(Solver2018Day25.YEAR, Solver2018Day25.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
