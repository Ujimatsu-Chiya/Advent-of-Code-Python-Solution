import re
from collections import defaultdict

from utils import Solver, get_data


class Solver2015Day19(Solver):
    YEAR = 2015
    DAY = 19

    def __init__(self, src):
        pat = re.compile(r"([A-Za-z]+)\s*=>\s*([A-Za-z]+)")
        self.mp = defaultdict(list)
        for l, r in pat.findall(src.strip()):
            self.mp[l].append(r)
        self.query = src.strip().split('\n')[-1]

    def solve_part_1(self):
        st = set()
        for k, v in self.mp.items():
            vec = self.query.split(k)
            for i in range(1, len(vec)):
                l, r = k.join(vec[:i]), k.join(vec[i:])
                for s in v:
                    st.add(l + s + r)
        return len(st)

    def solve_part_2(self):
        # https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4h7ji/?utm_source=share&utm_medium=web2x&context=3
        num_uppers = len([ch for ch in self.query if ch.isupper()])
        return num_uppers - self.query.count('Rn') - self.query.count('Ar') - self.query.count('Y') * 2 - 1


if __name__ == "__main__":
    src = get_data(Solver2015Day19.YEAR, Solver2015Day19.DAY)
    sol = Solver2015Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
