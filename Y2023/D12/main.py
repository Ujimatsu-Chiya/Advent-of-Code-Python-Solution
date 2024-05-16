from utils import Solver, get_data


class Solver2023Day12(Solver):
    YEAR = 2023
    DAY = 12

    def __init__(self, src):
        ls = []
        for s in src.strip().split('\n'):
            s, nums_str = s.split()
            lt = list(map(int, nums_str.split(',')))
            ls.append((s, lt))
        return ls

    def _solve(self, s, a):
        n, m = len(a), len(s)
        f = [[0 for _ in range(m)] for _ in range(n)]
        have_dot = [[False for _ in range(m + 1)] for _ in range(m + 1)]
        have_sign = [[False for _ in range(m + 1)] for _ in range(m + 1)]
        for l in range(m):
            have_dot[l][l] = (s[l] == '.')
            have_sign[l][l] = (s[l] == '#')
            for r in range(l + 1, m):
                have_dot[l][r] = (have_dot[l][r - 1] or s[r] == '.')
                have_sign[l][r] = (have_sign[l][r - 1] or s[r] == '#')
        for j in range(a[0] - 1, m):
            if not have_dot[j - a[0] + 1][j] and not have_sign[0][j - a[0]]:
                f[0][j] = 1
        for i in range(1, n):
            for j in range(a[i] - 1, m):
                if not have_dot[j - a[i] + 1][j]:
                    for k in range(a[i - 1] - 1, j - a[i]):
                        if not have_sign[k + 1][j - a[i]]:
                            f[i][j] += f[i - 1][k]
        ans = 0
        for j in range(m):
            if not have_sign[j + 1][m - 1]:
                ans += f[-1][j]
        return ans

    def solve_part_1(self):
        ans = 0
        ls = self.parse(src)
        for s, a in ls:
            ans += self._solve(s, a)
        return ans

    def solve_part_2(self):
        ans = 0
        ls = self.parse(src)
        for s, a in ls:
            ans += self._solve('?'.join([s] * 5), a * 5)
        return ans


if __name__ == "__main__":
    sol = Solver2023Day12()
    src = get_data(Solver2023Day12.YEAR, Solver2023Day12.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
