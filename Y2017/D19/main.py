from utils import Solver, get_data


class Solver2017Day19(Solver):
    YEAR = 2017
    DAY = 19

    def __init__(self, src):
        self.mp = src.rstrip('\n').split('\n')

    def _in_path(self, x, y):
        return 0 <= x < len(self.mp) and 0 <= y < len(self.mp[0]) and self.mp[x][y] != ' '

    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def solve_part_1(self):
        mp = self.mp
        x, y, d = 0, mp[0].index('|'), 0
        ans = ''
        while True:
            if not self._in_path(x + self.dirs[d][0], y + self.dirs[d][1]):
                d ^= 1
            x += self.dirs[d][0]
            y += self.dirs[d][1]
            while self._in_path(x, y) and mp[x][y] != '+':
                if mp[x][y].isalpha():
                    ans += mp[x][y]
                x += self.dirs[d][0]
                y += self.dirs[d][1]
            if mp[x][y] == '+':
                d ^= 2
            else:
                break
        return ans

    def solve_part_2(self):
        mp = self.mp
        n, m = len(mp), len(mp[0])

        return sum(1 + all(self._in_path(i + dx, j + dy) for dx, dy in self.dirs) for j in range(m) for i in range(n) if
                   self._in_path(i, j))


if __name__ == "__main__":
    src = get_data(Solver2017Day19.YEAR, Solver2017Day19.DAY)
    sol = Solver2017Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
