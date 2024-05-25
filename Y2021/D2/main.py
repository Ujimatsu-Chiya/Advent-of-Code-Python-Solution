from utils import Solver, get_data


class Solver2021Day2(Solver):
    YEAR = 2021
    DAY = 2

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            op, x = s.split()
            x = int(x)
            if op == 'forward':
                self.ops.append((1, x))
            else:
                self.ops.append((0, x if op == "down" else -x))

    def solve_part_1(self):
        c = [0, 0]
        for idx, val in self.ops:
            c[idx] += val
        return c[0] * c[1]

    def solve_part_2(self):
        dep = aim = s = 0
        for idx, val in self.ops:
            if idx == 0:
                aim += val
            else:
                s += val
                dep += aim * val
        return dep * s


if __name__ == "__main__":
    src = get_data(Solver2021Day2.YEAR, Solver2021Day2.DAY)
    sol = Solver2021Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
