import re
from collections import defaultdict

from tools import IntCodeComputer
from utils import Solver, get_data
from itertools import count


class Solver2019Day25(Solver):
    YEAR = 2019
    DAY = 25

    def __init__(self, src):
        self.ops = list(map(int, src.strip().split(',')))

    def solve_part_1(self):
        p = IntCodeComputer(self.ops)

        dirs = ['south', 'north', 'east', 'west']
        msg = p.get_ascii_output().strip()
        msg_mp = {}
        dir_mp = defaultdict(set)
        end_tag = '== Pressure-Sensitive Floor =='
        check_point_tag = '== Security Checkpoint =='
        end_path = []
        item_ls = []
        ban = {"escape pod", "photons", "molten lava", "infinite loop", "giant electromagnet"}
        pat = re.compile(r"Oh, hello! You should be able to get in by typing (\d+) on the keypad at the main airlock")

        def collect_items(msg):
            ls = msg.split("\n")
            if "Items here:" in ls:
                idx = ls.index("Items here:")
                for i in range(idx + 1, len(ls)):
                    if ls[i].startswith('-'):
                        s = ls[i].strip('- ')
                        if s not in ban:
                            item_ls.append(s)
                            p.add_ascii_input("take {}\n".format(s))
                            p.get_ascii_output()
                    else:
                        break

        def dfs(msg, st_dir):
            tag = msg.split('\n')[0]
            if tag in msg_mp.keys():
                return
            collect_items(msg)
            msg_mp[tag] = msg
            for i, d in enumerate(dirs):
                p.add_ascii_input(d + "\n")
                new_msg = p.get_ascii_output().strip()
                if new_msg.startswith('=='):
                    if new_msg.startswith(end_tag):
                        nonlocal end_path
                        end_path = st_dir + [d]
                        pos = new_msg.find(check_point_tag)
                        end_msg = new_msg[:pos].strip()
                        msg_mp[end_tag] = end_msg
                        dir_mp[tag].add((d, end_tag))
                        dir_mp[end_tag].add((dirs[i ^ 1], tag))
                    else:
                        next_tag = dfs(new_msg, st_dir + [d])
                        dir_mp[tag].add((d, next_tag))
                        dir_mp[next_tag].add((dirs[i ^ 1], tag))
                        p.add_ascii_input(dirs[i ^ 1] + "\n")
                        p.get_ascii_output()
            return tag

        dfs(msg, [])
        for d in end_path:
            p.add_ascii_input(d + "\n")
        n = len(item_ls)
        msk = (1 << n) - 2
        for st in range(msk, -1, -1):
            for i in range(n):
                if (st >> i & 1) == 0 and ((st + 1) >> i & 1) == 1:
                    p.add_ascii_input("drop {}\n".format(item_ls[i]))
                if (st >> i & 1) == 1 and ((st + 1) >> i & 1) == 0:
                    p.add_ascii_input("take {}\n".format(item_ls[i]))
            p.get_ascii_output()
            p.add_ascii_input(end_path[-1] + "\n")
            s = p.get_ascii_output()
            ls = pat.findall(s)
            if ls:
                return ls[0]

    def solve_part_2(self):
        pass


if __name__ == "__main__":
    src = get_data(Solver2019Day25.YEAR, Solver2019Day25.DAY)
    sol = Solver2019Day25(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
