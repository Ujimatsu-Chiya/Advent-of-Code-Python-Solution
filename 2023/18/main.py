from utils import Solver, get_data, Point

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
order = "RDLU"


class Solver2023Day18(Solver):
    YEAR = 2023
    DAY = 18

    def parse(self, src):
        ls = []
        for s in src.strip().split('\n'):
            dir, l, s = s.split()
            l = int(l)
            s = s[2:2 + 6]
            ls.append((dir, l, s))
        return ls

    def _solve(self, ls):
        x, y = 0, 0
        lt = [Point(x, y)]
        ans = premier = 0
        for dir, d in ls:
            x += dirs[dir][0] * d
            y += dirs[dir][1] * d
            premier += d
            lt.append(Point(x, y))
        n = len(lt)
        for i in range(n - 1):
            ans += lt[i] ^ lt[i + 1]
        return abs(ans) // 2 + premier // 2 + 1

    def solve_part_1(self, src):
        ls = self.parse(src)
        lt = []
        for dir, l, _ in ls:
            lt.append((dir, l))
        return self._solve(lt)

    def solve_part_2(self, src):
        ls = self.parse(src)
        lt = []
        for _, _, col in ls:
            l = int(col[:5], 16)
            lt.append((order[int(col[-1])], l))
        return self._solve(lt)


if __name__ == "__main__":
    sol = Solver2023Day18()
    src = get_data(Solver2023Day18.YEAR, Solver2023Day18.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
