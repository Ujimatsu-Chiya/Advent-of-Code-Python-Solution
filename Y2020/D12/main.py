from utils import Solver, get_data


class Solver2020Day12(Solver):
    YEAR = 2020
    DAY = 12

    dirs = [[1, 0], [0, -1], [-1, 0], [0, 1]]

    def __init__(self, src):
        self.queries = [[c[0], int(c[1:])] for c in src.strip().split()]

    def solve_part_1(self):

        x = y = p = 0
        for op, v in self.queries:
            if op in "LR":
                v = v // 90
                p = (p + v) % 4 if op == "R" else (p - v) % 4
            else:
                q = {'E': 0, 'S': 1, 'W': 2, 'N': 3}.get(op, p)
                x += self.dirs[q][0] * v
                y += self.dirs[q][1] * v
        return abs(x) + abs(y)

    def solve_part_2(self):
        x, y = 10, 1
        sx, sy = 0, 0
        for op, v in self.queries:
            if op in "LR":
                v = v // 90
                c = (-v if op == "R" else v) % 4
                for _ in range(c):
                    x, y = -y, x
            elif op == "F":
                sx += x * v
                sy += y * v
            else:
                q = {'E': 0, 'S': 1, 'W': 2, 'N': 3}[op]
                x += self.dirs[q][0] * v
                y += self.dirs[q][1] * v
        return abs(sx) + abs(sy)


if __name__ == "__main__":
    src = get_data(Solver2020Day12.YEAR, Solver2020Day12.DAY)
    sol = Solver2020Day12(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
