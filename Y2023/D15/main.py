from utils import Solver, get_data


class Solver2023Day15(Solver):
    YEAR = 2023
    DAY = 15

    def __init__(self, src):
        self.ls = src.strip().split(',')

    def solve_part_1(self):
        ans = 0
        for s in self.ls:
            w = 0
            for ch in s:
                w = (w + ord(ch)) * 17 % 256
            ans += w
        return ans

    def solve_part_2(self):
        mp = {}
        for i, s in enumerate(self.ls):
            if s.endswith('-'):
                tag = s.rstrip('-')
                if tag in mp.keys():
                    mp.pop(tag)
            else:
                tag, idx = s.split('=')
                idx = int(idx)
                if tag in mp.keys():
                    mp[tag] = (idx, mp[tag][1])
                else:
                    mp[tag] = (idx, i)
        M = 256
        box = [[] for _ in range(M)]
        for tag, t in mp.items():
            w = 0
            for ch in tag:
                w = (w + ord(ch)) * 17 % 256
            if len(t) > 0:
                idx, tm = t
                box[w].append((tm, idx, tag))
        ans = 0
        for id, b in enumerate(box):
            b.sort()
            for j in range(len(b)):
                ans += (id + 1) * (j + 1) * b[j][1]
        return ans


if __name__ == "__main__":
    src = get_data(Solver2023Day15.YEAR, Solver2023Day15.DAY)
    sol = Solver2023Day15(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
