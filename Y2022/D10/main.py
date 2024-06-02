from utils import Solver, get_data


class Solver2022Day10(Solver):
    YEAR = 2022
    DAY = 10

    def __init__(self, src):
        self.ops = []
        for s in src.strip().split('\n'):
            self.ops.append(list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())))
        self.ans1 = self.ans2 = None

    def run(self):
        vals = [1]
        for op in self.ops:
            if op[0] == 'noop':
                vals.append(vals[-1])
            else:
                vals.extend([vals[-1], vals[-1] + op[1]])
        queries = [20, 60, 100, 140, 180, 220]
        self.ans1 = sum(x * vals[x - 1] for x in queries)
        pts = []
        for i, x in enumerate(vals):
            pts.append(int(vals[i] - 1 <= i % 40 < vals[i] + 2))
        N, M = 6, 40
        ls = []
        for i in range(N):
            ls.append("".join(" #"[x] for x in pts[i*M:(i+1)*M]))
        self.ans2 = "\n".join(ls)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day10.YEAR, Solver2022Day10.DAY)
    sol = Solver2022Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
