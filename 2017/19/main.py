from utils import Solver, get_data


class Solver2017Day19(Solver):
    YEAR = 2017
    DAY = 19

    def parse(self, src):
        return src.rstrip('\n').split('\n')

    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def solve_part_1(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])

        def in_path(x, y):
            return 0 <= x < n and 0 <= y < m and mp[x][y] != ' '

        x, y, d = 0, mp[0].index('|'), 0
        ans = ''
        while True:
            if not in_path(x + self.dirs[d][0], y + self.dirs[d][1]):
                d ^= 1
            x += self.dirs[d][0]
            y += self.dirs[d][1]
            while in_path(x, y) and mp[x][y] != '+':
                if mp[x][y].isalpha():
                    ans += mp[x][y]
                x += self.dirs[d][0]
                y += self.dirs[d][1]
            if mp[x][y] == '+':
                d ^= 2
            else:
                break
        return ans

    def solve_part_2(self, src):
        mp = self.parse(src)
        n, m = len(mp), len(mp[0])

        def in_path(x, y):
            return 0 <= x < n and 0 <= y < m and mp[x][y] != ' '

        return sum(1 + all(in_path(i + dx, j + dy) for dx, dy in self.dirs) for j in range(m) for i in range(n) if
                   in_path(i, j))


if __name__ == "__main__":
    sol = Solver2017Day19()
    src = get_data(Solver2017Day19.YEAR, Solver2017Day19.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
