import re

import requests

from utils import Solver


class Solver18D17(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/17/input'

    def parse(self, src):
        clay = set()
        for line in src.strip().split('\n'):
            a, b0, b1 = map(int, re.findall(r'\d+', line))
            for b in range(b0, b1 + 1):
                clay.add((a, b) if line[0] == 'x' else (b, a))
        return clay

    def run(self, x, y, clay):

        mnx = min(x for x, y in clay)
        mxx = max(x for x, y in clay)
        mny = min(y for x, y in clay)
        mxy = max(y for x, y in clay)


        still, flowing = set(), set()

        # stop returns true if (x, y) has clay (horizontal scan stops here)
        def stop(x, y):
            return (x, y) in clay

        # fall scans downward until it hits clay or still water
        def fall(x, y):
            while y <= mxy and not pile(x, y + 1):
                flowing.add((x, y))
                y += 1
            if y <= mxy:
                flowing.add((x, y))
                queue.append((scan, x, y))

        # pile returns true if (x, y) is clay or still water (water can pile up here)
        def pile(x, y):
            return (x, y) in clay or (x, y) in still

        # scan looks left and right until it hits clay or falls off an edge
        def scan(x, y):
            x0 = x
            while pile(x0, y + 1) and not stop(x0 - 1, y):
                x0 -= 1
            x1 = x
            while pile(x1, y + 1) and not stop(x1 + 1, y):
                x1 += 1
            stop0 = stop(x0 - 1, y)
            stop1 = stop(x1 + 1, y)
            if stop0 and stop1:
                for i in range(x0, x1 + 1):
                    still.add((i, y))
                queue.append((scan, x, y - 1))
            else:
                for i in range(x0, x1 + 1):
                    flowing.add((i, y))
                if not stop0:
                    queue.append((fall, x0, y))
                if not stop1:
                    queue.append((fall, x1, y))

        # queue items are (func, *args)
        # queue is initially seeded with a fall at the (500, 0) starting point
        queue = []
        queue.append((fall, x, y))
        while queue:
            func, *args = queue.pop()
            func(*args)
        return still, flowing

    def solve_part_1(self, src):
        clay = self.parse(src)
        still, flowing = self.run(500, 0, clay)
        mny = min(v[1] for v in clay)
        mxy = max(v[1] for v in clay)
        return sum(1 for x, y in still | flowing if mny <= y <= mxy)

    def solve_part_2(self, src):
        clay = self.parse(src)
        still, _ = self.run(500, 0, clay)
        mny = min(v[1] for v in clay)
        mxy = max(v[1] for v in clay)
        return sum(1 for x, y in still if mny <= y <= mxy)


if __name__ == "__main__":
    sol = Solver18D17()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D17.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
