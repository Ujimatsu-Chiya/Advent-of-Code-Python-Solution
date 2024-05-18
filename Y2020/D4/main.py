import re

from utils import Solver, get_data


class Solver2020Day4(Solver):
    YEAR = 2020
    DAY = 4

    def __init__(self, src):
        ls = src.strip().split('\n\n')
        self.queries = []
        for t in ls:
            info = {}
            for s in t.split():
                key, val = s.split(':')
                info[key] = val
            self.queries.append(info)

    def solve_part_1(self):
        key_set = {'byr', 'iyr', 'eyr', 'hgt','hcl','ecl','pid'}
        return sum(1 for mp in self.queries if all(s in mp.keys() for s in key_set))

    def solve_part_2(self):
        pats = {
            "byr": re.compile(r"^(19[2-9][0-9]|200[0-2])$"),
            "iyr": re.compile(r"^(201[0-9]|2020)$"),
            "eyr": re.compile(r"^(202[0-9]|2030)$"),
            "hgt": re.compile(r"^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"),
            "hcl": re.compile(r"^#[0-9a-f]{6}$"),
            "ecl": re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$"),
            "pid": re.compile(r"^[0-9]{9}$")
        }
        return sum(1 for mp in self.queries if all(k in mp.keys() and pat.match(mp[k]) for k, pat in pats.items()))


if __name__ == "__main__":
    src = get_data(Solver2020Day4.YEAR, Solver2020Day4.DAY)
    sol = Solver2020Day4(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
