import re

import requests

from utils import Solver
from queue import Queue
from collections import defaultdict


class Solver16D10(Solver):
    INPUT_URL = 'https://adventofcode.com/2016/day/10/input'

    def parse(self, src):
        text = src.strip()
        pat_bot = re.compile(r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)")
        pat_value = re.compile(r"value (\d+) goes to bot (\d+)")
        bot_ops = pat_bot.findall(text)
        value_ops = pat_value.findall(text)
        return {int(v[0]): (v[1], int(v[2]), v[3], int(v[4])) for v in bot_ops}, \
               [list(map(int, v)) for v in value_ops]

    def solve_part_1(self, src):
        bot_ops, value_ops = self.parse(src)
        q = Queue()
        mp = defaultdict(list)
        output = {}
        for val, bot in value_ops:
            mp[bot].append(val)
        for k, v in mp.items():
            if len(v) == 2:
                q.put(k)
        while q.qsize() > 0:
            x = q.get()
            v = sorted(mp[x])
            if v == [17, 61]:
                return x
            op = bot_ops[x]
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

    def solve_part_2(self, src):
        bot_ops, value_ops = self.parse(src)
        q = Queue()
        mp = defaultdict(list)
        output = {}
        for val, bot in value_ops:
            mp[bot].append(val)
        for k, v in mp.items():
            if len(v) == 2:
                q.put(k)
        while q.qsize() > 0:
            x = q.get()
            v = sorted(mp[x])
            op = bot_ops[x]
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
        return output[0] * output[1] * output[2]


if __name__ == "__main__":
    sol = Solver16D10()
    session = open('../.session').read().strip()
    cookies = {'session': session}
    src = requests.get(Solver16D10.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
