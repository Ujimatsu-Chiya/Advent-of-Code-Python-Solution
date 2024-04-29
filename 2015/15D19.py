import requests

from utils import Solver
from collections import defaultdict


class Solver15D19(Solver):
    INPUT_URL = 'https://adventofcode.com/2015/day/19/input'

    def parse(self, src):
        query = ''
        mp = defaultdict(list)
        for s in src.strip().split('\n'):
            if "=>" in s:
                l, r = s.split(' => ')
                mp[l].append(r)
            elif s:
                query = s

        return query, mp

    def solve_part_1(self, src):
        query, mp = self.parse(src)
        st = set()
        for k, v in mp.items():
            vec = query.split(k)
            for i in range(1, len(vec)):
                l, r = k.join(vec[:i]), k.join(vec[i:])
                for s in v:
                    st.add(l + s + r)
        return len(st)

    def solve_part_2(self, src):
        # https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4h7ji/?utm_source=share&utm_medium=web2x&context=3
        query, _ = self.parse(src)
        num_uppers = len([ch for ch in query if ch.isupper()])
        return num_uppers - query.count('Rn') - query.count('Ar') - query.count('Y') * 2 - 1


if __name__ == "__main__":
    sol = Solver15D19()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver15D19.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
