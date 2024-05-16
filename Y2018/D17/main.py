import re

from utils import Solver, get_data


class Solver2018Day17(Solver):
    YEAR = 2018
    DAY = 17

    def __init__(self, src):
        self.clay = set()
        for line in src.strip().split('\n'):
            a, b0, b1 = map(int, re.findall(r'\d+', line))
            for b in range(b0, b1 + 1):
                self.clay.add((a, b) if line[0] == 'x' else (b, a))
        self.ans1 = self.ans2 = None

    def run(self):
        sx, sy = 500, 0
        mny = min(y for x, y in self.clay)
        mxy = max(y for x, y in self.clay)
        still, flowing = set(), set()
        scanned = set()

        def fall(x, y):
            while y <= mxy and not pile(x, y + 1):
                flowing.add((x, y))
                y += 1
            if y <= mxy:
                flowing.add((x, y))
                st.append((scan, x, y))

        def pile(x, y):
            return (x, y) in self.clay or (x, y) in still

        def scan(x, y):
            if (x, y) in scanned:
                return
            scanned.add((x, y))
            x0 = x
            while pile(x0, y + 1) and (x0 - 1, y) not in self.clay:
                x0 -= 1
            x1 = x
            while pile(x1, y + 1) and (x1 + 1, y) not in self.clay:
                x1 += 1
            stop0 = (x0 - 1, y) in self.clay
            stop1 = (x1 + 1, y) in self.clay
            if stop0 and stop1:
                for i in range(x0, x1 + 1):
                    still.add((i, y))
                st.append((scan, x, y - 1))
            else:
                for i in range(x0, x1 + 1):
                    flowing.add((i, y))
                if not stop0:
                    st.append((fall, x0, y))
                if not stop1:
                    st.append((fall, x1, y))

        st = [(fall, sx, sy)]
        while st:
            func, *args = st.pop()
            func(*args)
        self.ans1 = sum(1 for x, y in still | flowing if mny <= y <= mxy)
        self.ans2 = sum(1 for x, y in still if mny <= y <= mxy)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day17.YEAR, Solver2018Day17.DAY)
    sol = Solver2018Day17(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
