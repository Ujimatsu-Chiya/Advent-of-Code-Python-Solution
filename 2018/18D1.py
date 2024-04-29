import requests

from utils import Solver


class Solver18D1(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/1/input'

    def parse(self, src):
        return list(map(int, src.strip().split()))

    def solve_part_1(self, src):
        return sum(self.parse(src))

    def solve_part_2(self, src):
        a = self.parse(src)
        st = set()
        s = 0
        while True:
            for x in a:
                s += x
                if s in st:
                    return s
                st.add(s)


if __name__ == "__main__":
    sol = Solver18D1()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D1.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
