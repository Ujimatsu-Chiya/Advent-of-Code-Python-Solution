import requests

from utils import Solver


class Cart:
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def __init__(self, x, y, dir, cross):
        self.x, self.y = x, y
        self.dir = dir
        self.cross = cross

    def crash(self, other: 'Cart'):
        return self.x == other.x and self.y == other.y

    def go(self):
        self.x += Cart.dirs[self.dir][0]
        self.y += Cart.dirs[self.dir][1]

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.dir, self.cross)


class Solver18D13(Solver):
    INPUT_URL = 'https://adventofcode.com/2018/day/13/input'

    def parse(self, src):
        mp_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
        mp = src.strip('\n').split('\n')
        n, m = len(mp), len(mp[0])
        carts = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] in mp_dir:
                    carts.append(Cart(i, j, mp_dir[mp[i][j]], 0))
            mp[i] = mp[i].replace('<', '-').replace('>', '-').replace('^', '|').replace('v', '|')
        return carts, mp

    def _turn_cart(self, mp, c: Cart):
        if mp[c.x][c.y] == '+':
            if c.cross == 0:
                c.dir -= 1
            elif c.cross == 2:
                c.dir += 1
            c.cross = (c.cross + 1) % 3
        elif mp[c.x][c.y] == '\\':
            c.dir += -1 if c.dir % 2 == 0 else 1
        elif mp[c.x][c.y] == '/':
            c.dir += 1 if c.dir % 2 == 0 else -1
        c.dir &= 3

    def solve_part_1(self, src):
        carts, mp = self.parse(src)
        k = len(carts)
        while True:
            carts.sort(key=lambda cart: (cart.x, cart.y))
            # print(carts)
            for i in range(k):
                carts[i].go()
                self._turn_cart(mp, carts[i])
                if any(not (carts[i] is cart2) and carts[i].crash(cart2) for cart2 in carts):
                    return "{},{}".format(carts[i].y, carts[i].x)

    def solve_part_2(self, src):
        carts, mp = self.parse(src)
        while True:
            carts.sort(key=lambda cart: (cart.x, cart.y))
            if len(carts) == 1:
                return "{},{}".format(carts[0].y, carts[0].x)
            st = set()
            for i in range(len(carts)):
                if i in st:
                    continue
                carts[i].go()
                self._turn_cart(mp, carts[i])
                if any(not (carts[i] is cart2) and carts[i].crash(cart2) for cart2 in carts):
                    j = [j for j in range(len(carts)) if not (carts[i] is carts[j]) and carts[i].crash(carts[j])][0]
                    st |= {i, j}
            if st:
                carts = [carts[i] for i in range(len(carts)) if i not in st]


if __name__ == "__main__":
    sol = Solver18D13()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver18D13.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
