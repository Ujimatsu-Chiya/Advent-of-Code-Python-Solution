import requests

from utils import Solver


class Solver15D18(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/18/input'

    def _update_grid(self, pre):
        def count_on_neighbors(a, x, y):
            count = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(a) and 0 <= ny < len(a[0]):
                        if a[nx][ny] == '#':
                            count += 1
            return count

        now = [row.copy() for row in pre]
        for x in range(len(pre)):
            for y in range(len(pre[0])):
                on_neighbors = count_on_neighbors(pre, x, y)
                if pre[x][y] == '#' and not (2 <= on_neighbors <= 3):
                    now[x][y] = '.'
                elif pre[x][y] == '.' and on_neighbors == 3:
                    now[x][y] = '#'
        return now

    def parse(self, src):
        return [list(s) for s in src.strip().split()]

    def solve_part_1(self, src):
        a = self.parse(src)
        for i in range(100):
            a = self._update_grid(a)
        return sum(t.count('#') for t in a)

    def solve_part_2(self, src):
        a = self.parse(src)
        for i in range(100):
            a = self._update_grid(a)
            a[0][0] = a[0][-1] = a[-1][0] = a[-1][-1] = '#'
        return sum(t.count('#') for t in a)


if __name__ == "__main__":
    sol = Solver15D18()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D18.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
