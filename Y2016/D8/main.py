import re

from utils import Solver, get_data


class Solver2016Day8(Solver):
    YEAR = 2016
    DAY = 8

    def __init__(self, src):
        self.commands_ordered = []
        pat1 = re.compile(r"rect (\d+)x(\d+)")
        pat2 = re.compile(r"rotate row y=(\d+) by (\d+)")
        pat3 = re.compile(r"rotate column x=(\d+) by (\d+)")

        for line in src.strip().split('\n'):
            match1 = pat1.match(line)
            match2 = pat2.match(line)
            match3 = pat3.match(line)

            if match1:
                self. commands_ordered.append(("rect", int(match1.group(1)), int(match1.group(2))))
            elif match2:
                self.  commands_ordered.append(("rotate_row", int(match2.group(1)), int(match2.group(2))))
            elif match3:
                self. commands_ordered.append(("rotate_col", int(match3.group(1)), int(match3.group(2))))
        self.ans1 = self.ans2 = None

    def run(self):
        n, m = 6, 50
        a = [[0 for _ in range(m)] for _ in range(n)]
        for command, x, y in self.commands_ordered:
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
        self.ans1 = sum(sum(v) for v in a)
        self.ans2 = "\n".join("".join('#' if w else ' ' for w in u) for u in a)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day8.YEAR, Solver2016Day8.DAY)
    sol = Solver2016Day8(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
