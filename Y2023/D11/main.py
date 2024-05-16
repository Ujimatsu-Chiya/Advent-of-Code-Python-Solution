from utils import Solver, get_data


class Solver2023Day11(Solver):
    YEAR = 2023
    DAY = 11

    def __init__(self, src):
        return src.strip().split('\n')

    def solve_part_1(self):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        cx = [0 for _ in range(n)]
        cy = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    cx[i] += 1
                    cy[j] += 1

        kx = [int(w == 0) for w in cx]
        ky = [int(w == 0) for w in cy]
        for i in range(1, n):
            kx[i] += kx[i - 1]
        for j in range(1, m):
            ky[j] += ky[j - 1]
        ls = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    ls.append((i + kx[i], j + ky[j]))
        ans = 0
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                ans += abs(ls[i][0] - ls[j][0]) + abs(ls[i][1] - ls[j][1])
        return ans

    def solve_part_2(self):
        M = 1000000
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])
        cx = [0 for _ in range(n)]
        cy = [0 for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    cx[i] += 1
                    cy[j] += 1

        kx = [int(w == 0) for w in cx]
        ky = [int(w == 0) for w in cy]
        for i in range(1, n):
            kx[i] += kx[i - 1]
        for j in range(1, m):
            ky[j] += ky[j - 1]
        ls = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] == '#':
                    ls.append((i + kx[i] * (M - 1), j + ky[j] * (M - 1)))
        ans = 0
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                ans += abs(ls[i][0] - ls[j][0]) + abs(ls[i][1] - ls[j][1])
        return ans


if __name__ == "__main__":
    sol = Solver2023Day11()
    src = get_data(Solver2023Day11.YEAR, Solver2023Day11.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
