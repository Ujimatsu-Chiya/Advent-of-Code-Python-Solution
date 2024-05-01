import re
from operator import lt, eq, gt

from utils import Solver, get_data


class Solver2015Day16(Solver):
    YEAR = 2015
    DAY = 16

    item = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
            'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    def parse(self, src):
        pat1 = re.compile(r"Sue (\d+): ((?:\w+: \d+,?\s?)+)")
        pat2 = re.compile(r"(\w+): (\d+)")
        ls = []
        for idx, items_str in pat1.findall(src.strip()):
            item_list = pat2.findall(items_str)
            ls.append((int(idx), {k: int(v) for k, v in item_list}))
        return ls

    def solve_part_1(self, src):
        ls = self.parse(src)
        for idx, mp in ls:
            if all(mp[k] == self.item[k] for k, v in mp.items()):
                return idx

    def solve_part_2(self, src):
        op_list = {'children': eq, 'cats': gt, 'samoyeds': eq, 'pomeranians': lt, 'akitas': eq, 'vizslas': eq,
                   'goldfish': lt, 'trees': gt, 'cars': eq, 'perfumes': eq}
        ls = self.parse(src)
        for idx, mp in ls:
            if all(op_list[k](mp[k], self.item[k]) for k, v in mp.items()):
                return idx


if __name__ == "__main__":
    sol = Solver2015Day16()
    src = get_data(Solver2015Day16.YEAR, Solver2015Day16.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
