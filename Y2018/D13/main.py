from utils import Solver, get_data


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


class Solver2018Day13(Solver):
    YEAR = 2018
    DAY = 13

    def __init__(self, src):
        mp_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
        mp = src.strip('\n').split('\n')
        n, m = len(mp), len(mp[0])
        self.carts = []
        for i in range(n):
            for j in range(m):
                if mp[i][j] in mp_dir:
                    self.carts.append(Cart(i, j, mp_dir[mp[i][j]], 0))
            mp[i] = mp[i].replace('<', '-').replace('>', '-').replace('^', '|').replace('v', '|')
        self.mp = mp
        self.ans1 = self.ans2 = None

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

    def run(self):
        carts, mp = self.carts, self.mp
        while True:
            carts.sort(key=lambda cart: (cart.x, cart.y))
            if len(carts) == 1:
                self.ans2 = "{},{}".format(carts[0].y, carts[0].x)
                break
            st = set()
            for i in range(len(carts)):
                carts[i].go()
                self._turn_cart(mp, carts[i])
                if any(not (carts[i] is cart2) and carts[i].crash(cart2) for cart2 in carts):
                    if self.ans1 is None:
                        self.ans1 = "{},{}".format(carts[i].y, carts[i].x)
                    j = [j for j in range(len(carts)) if not (carts[i] is carts[j]) and carts[i].crash(carts[j])][0]
                    st |= {i, j}
            if st:
                carts = [carts[i] for i in range(len(carts)) if i not in st]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2018Day13.YEAR, Solver2018Day13.DAY)
    sol = Solver2018Day13(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
