import re
from collections import defaultdict
from queue import Queue

from utils import Solver, get_data


class Solver2016Day10(Solver):
    YEAR = 2016
    DAY = 10

    def __init__(self, src):
        text = src.strip()
        pat_bot = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")
        pat_value = re.compile(r"value (\d+) goes to bot (\d+)")
        bot_ops = pat_bot.findall(text)
        value_ops = pat_value.findall(text)
        self.bot_ops = {int(v[0]): (v[1], int(v[2]), v[3], int(v[4])) for v in bot_ops}
        self.value_ops = [list(map(int, v)) for v in value_ops]
        self.ans1 = self.ans2 = None

    def run(self):
        q = Queue()
        mp = defaultdict(list)
        output = {}
        for val, bot in self.value_ops:
            mp[bot].append(val)
        for k, v in mp.items():
            if len(v) == 2:
                q.put(k)
        while q.qsize() > 0:
            x = q.get()
            v = sorted(mp[x])
            if v == [17, 61]:
                self.ans1 = x
            op = self.bot_ops[x]
            if op[0] == "bot":
                mp[op[1]].append(v[0])
                if len(mp[op[1]]) == 2:
                    q.put(op[1])
            else:
                output[op[1]] = v[0]
            if op[2] == "bot":
                mp[op[3]].append(v[1])
                if len(mp[op[3]]) == 2:
                    q.put(op[3])
            else:
                output[op[3]] = v[1]
        self.ans2 = output[0] * output[1] * output[2]

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2016Day10.YEAR, Solver2016Day10.DAY)
    sol = Solver2016Day10(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
