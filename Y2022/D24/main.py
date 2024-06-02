from utils import Solver, get_data
from itertools import count


class Solver2022Day24(Solver):
    YEAR = 2022
    DAY = 24

    def __init__(self, src):
        self.mp = src.strip().split('\n')
        self.ans1 = self.ans2 = None

    def run(self):
        n, m = len(self.mp), len(self.mp[0])
        block = [[[set(), set()] for _ in range(m)] for _ in range(n)]
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                for x in range(1, n - 1):
                    if self.mp[x][j] == '^':
                        block[i][j][0].add((x - i) % (n - 2))
                    elif self.mp[x][j] == 'v':
                        block[i][j][0].add((i - x) % (n - 2))
                for y in range(1, m - 1):
                    if self.mp[i][y] == '<':
                        block[i][j][1].add((y - j) % (m - 2))
                    elif self.mp[i][y] == '>':
                        block[i][j][1].add((j - y) % (m - 2))

        p_st = (0, self.mp[0].find('.'))
        p_ed = (n - 1, self.mp[-1].find('.'))
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1], [0, 0]]

        def que(start, p_st, p_ed):
            st = {p_st}
            for t in count(start + 1):
                if p_ed in st:
                    return t
                su = set()
                for sx, sy in st:
                    for dx, dy in dirs:
                        x, y = sx + dx, sy + dy
                        if 0 <= x < n and 0 <= y < m and self.mp[x][y] != '#' and \
                                t % (n - 2) not in block[x][y][0] and t % (m - 2) not in block[x][y][1]:
                            su.add((x, y))
                st = su
                if p_ed in st:
                    return t

        self.ans1 = que(0, p_st, p_ed)
        t = que(self.ans1, p_ed, p_st)
        self.ans2 = que(t, p_st, p_ed)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day24.YEAR, Solver2022Day24.DAY)
    sol = Solver2022Day24(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
