from utils import Solver, get_data


class Solver2021Day13(Solver):
    YEAR = 2021
    DAY = 13

    def __init__(self, src):
        p_str, fold_str = src.strip().split('\n\n')
        self.p_ls = [list(map(int, s.split(','))) for s in p_str.split()]
        self.fold_op = []
        for s in fold_str.split('\n'):
            l, r = s.split('=')
            self.fold_op.append([l[-1], int(r)])
        self.ans1 = self.ans2 = None

    def run(self):
        st = set(tuple(v) for v in self.p_ls)
        for op, w in self.fold_op:
            if op == 'y':
                st = {(x, w - abs(w - y)) for x, y in st}
            else:
                st = {(w - abs(w - x), y) for x, y in st}
            if self.ans1 is None:
                self.ans1 = len(st)
        mxy = max(v[0] for v in st)
        mxx = max(v[1] for v in st)
        self.ans2 = "\n".join("".join('#' if (j, i) in st else ' ' for j in range(mxy + 1)) for i in range(mxx + 1))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day13.YEAR, Solver2021Day13.DAY)
    #     src = '''6,10
    # 0,14
    # 9,10
    # 0,3
    # 10,4
    # 4,11
    # 6,0
    # 6,12
    # 4,1
    # 0,13
    # 10,12
    # 3,4
    # 3,0
    # 8,4
    # 1,10
    # 2,14
    # 8,10
    # 9,0
    #
    # fold along y=7
    # fold along x=5'''
    sol = Solver2021Day13(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
