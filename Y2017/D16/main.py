from itertools import count

from utils import Solver, get_data


class Solver2017Day16(Solver):
    YEAR = 2017
    DAY = 16

    def __init__(self, src):
        ls = []
        for s in src.strip().split(','):
            if s[0] == 's':
                ls.append([s[0], int(s[1:])])
            elif s[0] == 'x':
                A, B = map(int, s[1:].split('/'))
                ls.append([s[0], A, B])
            else:
                A, B = s[1:].split('/')
                ls.append([s[0], A, B])
        self.ops = ls

    def _solve(self, ls, s):
        a = list(s)
        for ins in ls:
            if ins[0] == 's':
                a = a[-ins[1]:] + a[:-ins[1]]
            elif ins[0] == 'x':
                x, y = ins[1], ins[2]
                a[x], a[y] = a[y], a[x]
            else:
                c1, c2 = ins[1], ins[2]
                x, y = a.index(c1), a.index(c2)
                a[x], a[y] = a[y], a[x]
        return "".join(a)

    def solve_part_1(self):
        s = "abcdefghijklmnop"
        return self._solve(self.ops, s)

    def solve_part_2(self):
        s = "abcdefghijklmnop"
        M = 10 ** 9
        mp = {}
        state_ls = []
        st = T = -1
        for i in count():
            if s in mp.keys():
                T = i - mp[s]
                st = mp[s]
                break
            mp[s] = i
            state_ls.append(s)
            s = self._solve(self.ops, s)
        if M <= st:
            idx = M
        else:
            idx = st + (M - st) % T
        return state_ls[idx]


if __name__ == "__main__":
    src = get_data(Solver2017Day16.YEAR, Solver2017Day16.DAY)
    sol = Solver2017Day16(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
