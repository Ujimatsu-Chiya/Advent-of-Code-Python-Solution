import requests

from utils import Solver


class Solver16D1(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/1/input'
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def parse(self, src):
        ls = src.strip().split(', ')
        return [[s[0], int(s[1:])] for s in ls]

    def solve_part_1(self, src):
        ls = self.parse(src)
        x = y = p = 0
        for d, dis in ls:
            if d == 'L':
                p = (p - 1) % 4
            else:
                p = (p + 1) % 4
            x += self.dirs[p][0] * dis
            y += self.dirs[p][1] * dis
        return abs(x) + abs(y)

    def solve_part_2(self, src):
        ls = self.parse(src)
        st = {(0, 0)}
        x = y = p = 0
        for d, dis in ls:
            if d == 'L':
                p = (p - 1) % 4
            else:
                p = (p + 1) % 4
            for k in range(dis):
                x += self.dirs[p][0]
                y += self.dirs[p][1]
                if (x, y) in st:
                    return abs(x) + abs(y)
                st.add((x, y))
        return None


if __name__ == "__main__":
    sol = Solver16D1()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D1.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
