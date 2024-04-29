import re

import requests

from utils import Solver
from operator import lt, eq, gt


class Solver15D16(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/16/input'
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
    sol = Solver15D16()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D16.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
