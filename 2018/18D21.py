import re

import requests

from utils import Solver


class Solver18D21(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/21/input'

    def parse(self, src):
        pat1 = re.compile(r'(\w+) (\d+) (\d+) (\d+)')
        ls = []
        for tp in pat1.findall(src.strip()):
            ls.append([tp[0]] + list(map(int, tp[1:])))
        pat2 = re.compile(r'#ip (\d+)')
        ip = int(pat2.findall(src.strip())[0])
        return ip, ls

    def solve_part_1(self, src):
        ip, ls = self.parse(src)
        n = ls[7][1]
        c = 0
        while True:
            a = c | 65536
            c = n
            while True:
                c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
                if 256 > a:
                    return c
                else:
                    a //= 256

    def solve_part_2(self, src):
        ip, ls = self.parse(src)
        n = ls[7][1]
        st = set()
        c = 0
        last_unique_c = -1
        while True:
            a = c | 65536
            c = n
            while True:
                c = (((c + (a & 255)) & 16777215) * 65899) & 16777215
                if 256 > a:
                    if c not in st:
                        st.add(c)
                        last_unique_c = c
                        break
                    else:
                        return last_unique_c
                else:
                    a //= 256


if __name__ == "__main__":
    sol = Solver18D21()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D21.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
