from itertools import cycle, count

from utils import Solver, get_data


class Solver2022Day17(Solver):
    YEAR = 2022
    DAY = 17

    def __init__(self, src):
        self.ops = [{'<': -1, '>': 1}[ch] for ch in src.strip()]
        self.ans1 = self.ans2 = None

    def run(self):
        rock = [[(0, 2), (0, 3), (0, 4), (0, 5)],
                [(1, 2), (0, 3), (1, 3), (2, 3), (1, 4)],
                [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
                [(0, 2), (1, 2), (2, 2), (3, 2)],
                [(0, 2), (0, 3), (1, 2), (1, 3)]]
        M = 7
        block = {(0, i) for i in range(M)}
        mx = 0
        mp = {}
        state_ls = []
        j = 0
        sum_x = sum(max(v[0] for v in r) + 1 for r in rock) * 2
        st = T = -1
        for i in count():
            key = i % len(rock), j % len(self.ops), tuple((mx - i, j) in block for i in range(sum_x) for j in range(M))
            if key in mp.keys():
                T = i - mp[key]
                st = mp[key]
                break
            mp[key] = i
            pos = [(mx + x + 3 + 1, y) for x, y in rock[i % len(rock)]]
            while True:
                dy = self.ops[j % len(self.ops)]
                j += 1
                tmp = [(x, y + dy) for x, y in pos]
                if tmp[0][1] >= 0 and tmp[-1][1] < M and all(tp not in block for tp in tmp):
                    pos = tmp
                tmp = [(x - 1, y) for x, y in pos]
                if any(tp in block for tp in tmp):
                    break
                pos = tmp
            pre = mx
            mx = max(mx, max(v[0] for v in pos))
            state_ls.append(mx - pre)
            block |= set(pos)

        def que(Q):
            if Q <= st:
                return sum(state_ls[:Q])
            else:
                q, m = divmod(Q - st, T)
                d = sum(state_ls[st:])
                return sum(state_ls[:st + m]) + d * q

        self.ans1 = que(2022)
        self.ans2 = que(1000000000000)

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2022Day17.YEAR, Solver2022Day17.DAY)
    sol = Solver2022Day17(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
