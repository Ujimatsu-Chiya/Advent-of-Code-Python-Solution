import re
import operator

from utils import Solver, get_data


class Solver2015Day16(Solver):
    YEAR = 2015
    DAY = 16

    item = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
            'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

    def __init__(self, src):
        pat1 = re.compile(r"Sue (\d+): ((?:\w+: \d+,?\s?)+)")
        pat2 = re.compile(r"(\w+): (\d+)")
        self.ls = []
        for idx, items_str in pat1.findall(src.strip()):
            item_list = pat2.findall(items_str)
            self.ls.append((int(idx), {k: int(v) for k, v in item_list}))

    def solve_part_1(self):
        for idx, mp in self.ls:
            if all(mp[k] == self.item[k] for k, v in mp.items()):
                return idx

    def solve_part_2(self):
        op_list = {'children': operator.eq, 'cats': operator.gt, 'samoyeds': operator.eq, 'pomeranians': operator.lt,
                   'akitas': operator.eq, 'vizslas': operator.eq, 'goldfish': operator.lt, 'trees': operator.gt,
                   'cars': operator.eq, 'perfumes': operator.eq}
        for idx, mp in self.ls:
            if all(op_list[k](mp[k], self.item[k]) for k, v in mp.items()):
                return idx


if __name__ == "__main__":
    src = get_data(Solver2015Day16.YEAR, Solver2015Day16.DAY)
    sol = Solver2015Day16(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
