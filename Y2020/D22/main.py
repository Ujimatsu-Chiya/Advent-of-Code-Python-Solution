from collections import deque
from itertools import islice

from utils import Solver, get_data


class Solver2020Day22(Solver):
    YEAR = 2020
    DAY = 22

    def __init__(self, src):
        p_str = src.strip().split('\n\n')
        self.cards = [list(map(int, s.split('\n')[1:])) for s in p_str]

    def _run(self, q, recursive=False):
        vis = set()
        while len(q[0]) > 0 and len(q[1]) > 0:
            if (tuple(q[0]), tuple(q[1])) in vis:
                return 0, 0
            # print(q[0], q[1])
            vis.add((tuple(q[0]), tuple(q[1])))
            val = (q[0].popleft(), q[1].popleft())
            if val[0] <= len(q[0]) and val[1] <= len(q[1]) and recursive:
                _, p = self._run([deque(islice(q[0], val[0])), deque(islice(q[1], val[1]))], recursive)
            else:
                p = int(val[1] > val[0])

            q[p].append(val[p])
            q[p].append(val[p ^ 1])
        winner = 0 if q[0] else 1
        return sum((len(q[winner]) - i) * x for i, x in enumerate(q[winner])), winner

    def solve_part_1(self):
        return self._run([deque(ls) for ls in self.cards], False)[0]

    def solve_part_2(self):
        return self._run([deque(ls) for ls in self.cards], True)[0]


if __name__ == "__main__":
    src = get_data(Solver2020Day22.YEAR, Solver2020Day22.DAY)
    sol = Solver2020Day22(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
