import re

from utils import Solver, get_data


class Solver2018Day21(Solver):
    YEAR = 2018
    DAY = 21

    def __init__(self, src):
        pat1 = re.compile(r'(\w+) (\d+) (\d+) (\d+)')
        self.ops = []
        for tp in pat1.findall(src.strip()):
            self.ops.append([tp[0]] + list(map(int, tp[1:])))
        pat2 = re.compile(r'#ip (\d+)')
        self.ip = int(pat2.findall(src.strip())[0])
        self.ans1 = self.ans2 = None

    def run(self):
        n = self.ops[7][1]
        ls = []
        st = set()
        c = 0
        while True:
            a = c | 65536
            c = n
            while True:
                c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
                if a < 256:
                    if c in st:
                        self.ans1 = ls[0]
                        self.ans2 = ls[-1]
                        return
                    else:
                        ls.append(c)
                        st.add(c)
                        break
                else:
                    a >>= 8

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day21.YEAR, Solver2018Day21.DAY)
    sol = Solver2018Day21(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
