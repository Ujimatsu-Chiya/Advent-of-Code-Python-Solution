import re
from collections import defaultdict

import requests

from utils import Solver


class Solver17D25(Solver):
    INPUT_URL = 'https://adventofcode.com/2017/day/25/input'

    def parse(self, src):
        pat1 = re.compile(r"Begin in state (\w+).\s*Perform a diagnostic checksum after (\d+) steps.")
        pat2 = re.compile(r"In state (\w+):\s*" + \
                          r"If the current value is 0:\s*" + \
                          r"- Write the value (\d+).\s*" + \
                          r"- Move one slot to the (\w+).\s*" + \
                          r"- Continue with state (\w+).\s*" + \
                          r"If the current value is 1:\s*" + \
                          r"- Write the value (\d+).\s*" + \
                          r"- Move one slot to the (\w+).\s*" + \
                          r"- Continue with state (\w+).")
        mp = {}
        match = pat1.search(src.strip())
        state = match.group(1)
        steps = int(match.group(2))
        for t in pat2.findall(src.strip()):
            mp[t[0]] = [(int(t[1]), 1 if t[2][0] == 'r' else -1, t[3]),
                        (int(t[4]), 1 if t[5][0] == 'r' else -1, t[6])]
        return state, steps, mp

    def solve_part_1(self, src):
        state, steps, mp = self.parse(src)
        tape = defaultdict(int)
        pos = 0
        for _ in range(steps):
            x = tape[pos]
            tape[pos] = mp[state][x][0]
            pos += mp[state][x][1]
            state = mp[state][x][2]
        return sum(tape.values())

    def solve_part_2(self, src):
        pass


if __name__ == "__main__":
    sol = Solver17D25()
    session = open('../.session').read().strip()
    cookies = {'session': session}

    src = requests.get(Solver17D25.INPUT_URL, cookies=cookies).text
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))