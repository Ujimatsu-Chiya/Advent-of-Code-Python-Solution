from utils import Solver, get_data


class Solver2023Day2(Solver):
    YEAR = 2023
    DAY = 2

    def parse(self, src):
        ls = []
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
            ls.append((idx, mp))
        return ls

    def solve_part_1(self, src):
        max_col = {'red': 12, 'green': 13, 'blue': 14}
        ans = 0
        for idx, mp in self.parse(src):
            if all(mp.get(col, 0) <= cnt for col, cnt in max_col.items()):
                ans += idx
        return ans

    def solve_part_2(self, src):
        ans = 0
        for idx, mp in self.parse(src):
            ans += mp.get('red', 0) * mp.get('green', 0) * mp.get('blue', 0)
        return ans


if __name__ == "__main__":
    sol = Solver2023Day2()
    src = get_data(Solver2023Day2.YEAR, Solver2023Day2.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
