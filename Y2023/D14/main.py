from itertools import count

from utils import Solver, get_data


class Solver2023Day14(Solver):
    YEAR = 2023
    DAY = 14

    def __init__(self, src):
        self.ls =  [list(s) for s in src.strip().split('\n')]

    def solve_part_1(self):
        n, m = len(self.ls), len(self.ls[0])
        ans = 0
        for j in range(m):
            now = -1
            for i in range(n):
                if self.ls[i][j] == 'O':
                    now += 1
                    ans += n - now
                elif self.ls[i][j] == '#':
                    now = i
        return ans

    def solve_part_2(self):
        ls = self.ls
        M = 1000000000
        mp = {}
        state_ls = []
        st = T = -1
        for i in count():
            tp = tuple(tuple(s) for s in ls)
            if tp in mp.keys():
                T = i - mp[tp]
                st = mp[tp]
                break
            mp[tp] = i
            state_ls.append(tp)
            for _ in range(4):
                n, m = len(ls), len(ls[0])
                for j in range(m):
                    now = -1
                    for i in range(n):
                        if ls[i][j] == 'O':
                            ls[i][j] = '.'
                            now += 1
                            ls[now][j] = 'O'
                        elif ls[i][j] == '#':
                            now = i
                lt = [['' for _ in range(n)] for _ in range(m)]
                for i in range(n):
                    for j in range(m):
                        lt[j][i] = ls[i][j]
                for i in range(m):
                    lt[i].reverse()
                ls = lt
        if st >= M:
            idx = M
        else:
            idx = st + (M - st) % T
        board = state_ls[idx]
        ans = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    ans += len(board) - i
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day14.YEAR, Solver2023Day14.DAY)
    sol = Solver2023Day14(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
