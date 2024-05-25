from math import prod

from utils import Solver, get_data


class Solver2021Day16(Solver):
    YEAR = 2021
    DAY = 16

    def __init__(self, src):
        mp = {ch: "{:04b}".format(int(ch, 16)) for ch in "0123456789ABCDEF"}
        self.s = "".join(mp[ch] for ch in src.strip())
        self.ans1 = self.ans2 = None

    def run(self):
        s = self.s
        self.ans1 = 0

        def dfs(i):
            version, op = int(s[i:i + 3], 2), int(s[i + 3:i + 6], 2)
            self.ans1 += version
            if op == 4:
                p = i + 6
                t = ''
                while p < len(s):
                    t += s[p + 1:p + 5]
                    if s[p] == '0':
                        break
                    p += 5
                return p + 5 - i, int(t, 2)
            else:
                nums = []
                mod = int(s[i + 6])
                if mod == 0:
                    length = int(s[i + 7:i + 22], 2)
                    p = i + 22
                    while p < i + 22 + length:
                        sz, val = dfs(p)
                        p += sz
                        nums.append(val)
                else:
                    rounds = int(s[i + 7:i + 7 + 11], 2)
                    p = i + 18
                    for _ in range(rounds):
                        sz, val = dfs(p)
                        p += sz
                        nums.append(val)
                match op:
                    case 0:
                        res = sum(nums)
                    case 1:
                        res = prod(nums)
                    case 2:
                        res = min(nums)
                    case 3:
                        res = max(nums)
                    case 5:
                        res = int(nums[0] > nums[1])
                    case 6:
                        res = int(nums[0] < nums[1])
                    case 7:
                        res = int(nums[0] == nums[1])
                return p - i, res

        self.ans2 = dfs(0)[1]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2021Day16.YEAR, Solver2021Day16.DAY)
    sol = Solver2021Day16(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
