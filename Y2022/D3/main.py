from utils import Solver, get_data
from string import ascii_lowercase, ascii_uppercase


class Solver2022Day3(Solver):
    YEAR = 2022
    DAY = 3
    pos = {ch: i + 1 for i, ch in enumerate(ascii_lowercase + ascii_uppercase)}

    def __init__(self, src):
        self.queries = src.strip().split()

    def solve_part_1(self):
        return sum(sum(self.pos[ch] for ch in set(s[:len(s) >> 1]) & set(s[len(s) >> 1:])) for s in self.queries)

    def solve_part_2(self):
        return sum(sum(self.pos[ch] for ch in set.intersection(*map(set, self.queries[i:i + 3]))) for i in range(0, len(self.queries), 3))


if __name__ == "__main__":
    src = get_data(Solver2022Day3.YEAR, Solver2022Day3.DAY)
    sol = Solver2022Day3(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
