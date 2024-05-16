from utils import Solver, get_data


class Solver2016Day16(Solver):
    YEAR = 2016
    DAY = 16

    def __init__(self, src):
        self.s = src.strip()

    def _run(self, M):
        s = self.s
        while len(s) < M:
            s = s + "0" + "".join(['1' if ch == '0' else '0' for ch in s[::-1]])
        s = s[:M]
        while len(s) % 2 == 0:
            s = "".join(['1' if s[i] == s[i + 1] else '0' for i in range(0, len(s), 2)])
        return s

    def solve_part_1(self):
        return self._run(272)

    def solve_part_2(self):
        return self._run(35651584)


if __name__ == "__main__":
    src = get_data(Solver2016Day16.YEAR, Solver2016Day16.DAY)
    sol = Solver2016Day16(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
