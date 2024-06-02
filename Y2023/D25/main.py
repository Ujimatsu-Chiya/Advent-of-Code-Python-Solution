from random import sample

import networkx as nx

from utils import Solver, get_data


class Solver2023Day25(Solver):
    YEAR = 2023
    DAY = 25

    def __init__(self, src):
        self.g = nx.Graph()
        for s in src.strip().split('\n'):
            key, val_str = s.split(': ')
            for val in val_str.split():
                self.g.add_edge(key, val, capacity=1)

    def solve_part_1(self):
        nodes = list(self.g.nodes)
        while True:
            cnt, cuts = nx.minimum_cut(self.g, *sample(nodes, 2))
            if cnt == 3:
                return len(cuts[0]) * len(cuts[1])

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2023Day25.YEAR, Solver2023Day25.DAY)
    sol = Solver2023Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
