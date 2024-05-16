from tools import mod_inverse
from utils import Solver, get_data


class Solver2019Day22(Solver):
    YEAR = 2019
    DAY = 22

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            ls = s.split()
            if ls[-1][-1].isdigit():
                self.ops.append((ls[0], int(ls[-1])))
            else:
                self.ops.append(("reversed", -1))

    def queries(self, n):
        k, b = 1, 0
        for op, v in self.ops:
            if op == "reversed":
                k, b = -k, -b - 1
            elif op == "cut":
                b -= v
            else:
                k *= v
                b *= v
            k %= n
            b %= n
        return k, b

    def solve_part_1(self):
        n = 10007
        x = 2019
        M = 1
        k, b = self.queries(n)
        return (pow(k, M, n) * x + (pow(k, M, n) - 1) * mod_inverse(k - 1, n) * b) % n

    def solve_part_2(self):
        n = 119315717514047
        p = 2020
        M = 101741582076661

        k, b = self.queries(n)
        return (p * (k - 1) - (pow(k, M, n) - 1) * b) * mod_inverse((k - 1) * pow(k, M, n), n) % n


if __name__ == "__main__":
    src = get_data(Solver2019Day22.YEAR, Solver2019Day22.DAY)
    sol = Solver2019Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
