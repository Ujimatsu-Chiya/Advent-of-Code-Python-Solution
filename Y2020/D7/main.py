import re

from utils import Solver, get_data
from collections import defaultdict, deque


class Solver2020Day7(Solver):
    YEAR = 2020
    DAY = 7

    def __init__(self, src):
        pat1 = re.compile(r'^([a-z ]+ bags?) contain (.+)\.$')
        pat2 = re.compile(r'(\d+) ([a-z ]+ bags?)')
        self.data = {}
        for s in src.strip().split('\n'):
            line_match = pat1.match(s)
            if line_match:
                bag = line_match.group(1).replace(' bags', '').replace(' bag', '')
                contents = line_match.group(2)
                if contents == 'no other bags':
                    self.data[bag] = []
                else:
                    content_matches = pat2.findall(contents)
                    self.data[bag] = [(int(count), bag.replace(' bags', '').replace(' bag', '')) for count, bag in
                                      content_matches]

        # self.data = defaultdict(list)
        # self.bag_st = set()
        # for s in src.strip().split('\n'):
        #     line_match = pat1.match(s)
        #     if line_match:
        #         bag = line_match.group(1).replace(' bags', '').replace(' bag', '')
        #         self.bag_st.add(bag)
        #         contents = line_match.group(2)
        #         if contents == 'no other bags':
        #             self.data[bag] = []
        #         else:
        #             content_matches = pat2.findall(contents)
        #             for cnt, new_bag in content_matches:
        #                 cnt, new_bag = int(cnt), new_bag.replace(' bags', '').replace(' bag', '')
        #                 self.data[new_bag].append((cnt, bag))

    def solve_part_1(self):
        start = "shiny gold"
        g = defaultdict(list)
        for u, msg in self.data.items():
            for _, v in msg:
                g[v].append(u)
        q = deque([start])
        st = {start}
        while len(q) > 0:
            u = q.popleft()
            for v in g[u]:
                if v not in st:
                    st.add(v)
                    q.append(v)
        return len(st) - 1

    def solve_part_2(self):
        start = "shiny gold"
        deg,f = defaultdict(int),defaultdict(int)
        for u, msg in self.data.items():
            for _, v in msg:
                deg[v] += 1
        q = deque()
        f[start] = 1
        for u in self.data.keys():
            if deg[u] == 0:
                q.append(u)
        while len(q) > 0:
            u = q.popleft()
            for cnt, v in self.data[u]:
                f[v] += f[u] * cnt
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        return sum(f.values()) - 1


if __name__ == "__main__":
    src = get_data(Solver2020Day7.YEAR, Solver2020Day7.DAY)
#     src = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''
    sol = Solver2020Day7(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
