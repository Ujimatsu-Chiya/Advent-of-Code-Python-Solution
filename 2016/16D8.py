import re

import requests

from utils import Solver


class Solver16D8(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/8/input'

    def parse(self, src):
        commands_ordered = []
        rect_pattern = r"rect (\d+)x(\d+)"
        rotate_row_pattern = r"rotate row y=(\d+) by (\d+)"
        rotate_col_pattern = r"rotate column x=(\d+) by (\d+)"

        for line in src.strip().split('\n'):
            rect_match = re.match(rect_pattern, line)
            rotate_row_match = re.match(rotate_row_pattern, line)
            rotate_col_match = re.match(rotate_col_pattern, line)

            if rect_match:
                commands_ordered.append(("rect", int(rect_match.group(1)), int(rect_match.group(2))))
            elif rotate_row_match:
                commands_ordered.append(("rotate_row", int(rotate_row_match.group(1)), int(rotate_row_match.group(2))))
            elif rotate_col_match:
                commands_ordered.append(("rotate_col", int(rotate_col_match.group(1)), int(rotate_col_match.group(2))))
        return commands_ordered

    def _solve(self, ls):
        n, m = 6, 50
        a = [[0 for _ in range(m)] for _ in range(n)]
        for command, x, y in ls:
            if command == 'rect':
                for i in range(y):
                    for j in range(x):
                        a[i][j] = 1
            elif command == 'rotate_row':
                a[x] = [a[x][(j - y) % m] for j in range(m)]
            else:
                t = [a[i][x] for i in range(n)]
                t = [t[(i - y) % n] for i in range(n)]
                for i in range(n):
                    a[i][x] = t[i]
        return a

    def solve_part_1(self, src):
        a = self._solve(self.parse(src))
        return sum(sum(v) for v in a)

    def solve_part_2(self, src):
        a = self._solve(self.parse(src))
        return "\n".join("".join('#' if w else ' ' for w in u) for u in a)


if __name__ == "__main__":
    sol = Solver16D8()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D8.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
