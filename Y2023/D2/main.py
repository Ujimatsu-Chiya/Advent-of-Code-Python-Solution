from utils import Solver, get_data


class Solver2023Day2(Solver):
    YEAR = 2023
    DAY = 2

    def __init__(self, src):
        self.queries = []
        for s in src.strip().split('\n'):
            idx, info_str = s.split(':')
            idx = int(idx.split()[-1])
            info_ls = info_str.strip().split('; ')
            mp = dict()
            for info in info_ls:
                tp = info.split(', ')
                for s in tp:
                    cnt, col = s.split()
                    cnt = int(cnt)
                    mp[col] = max(mp.get(col, 0), cnt)
            self.queries.append((idx, mp))

    def solve_part_1(self):
        max_col = {'red': 12, 'green': 13, 'blue': 14}
        return sum(idx for idx, mp in self.queries if all(mp.get(col, 0) <= cnt for col, cnt in max_col.items()))

    def solve_part_2(self):
        return sum(mp.get('red', 0) * mp.get('green', 0) * mp.get('blue', 0) for _, mp in self.queries)


if __name__ == "__main__":
    src = get_data(Solver2023Day2.YEAR, Solver2023Day2.DAY)
    sol = Solver2023Day2(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
