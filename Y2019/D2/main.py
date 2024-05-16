from utils import Solver, get_data


class Solver2019Day2(Solver):
    YEAR = 2019
    DAY = 2

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def _run(self, ops, x, y):
        ops[1] = x
        ops[2] = y
        for i in range(0, len(ops), 4):
            if ops[i] == 1:
                ops[ops[i + 3]] = ops[ops[i + 1]] + ops[ops[i + 2]]
            elif ops[i] == 2:
                ops[ops[i + 3]] = ops[ops[i + 1]] * ops[ops[i + 2]]
            elif ops[i] == 99:
                break
            else:
                return -1
        return ops[0]

    def solve_part_1(self):
        return self._run(self.ops.copy(), 12, 2)

    def solve_part_2(self):
        M = 100
        m = 19690720
        for x in range(M):
            for y in range(M):
                if self._run(self.ops.copy(), x, y) == m:
                    return x * 100 + y


if __name__ == "__main__":
    src = get_data(Solver2019Day2.YEAR, Solver2019Day2.DAY)
    sol = Solver2019Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
