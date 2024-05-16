import re

from utils import Solver, get_data


class Solver2023Day19(Solver):
    YEAR = 2023
    DAY = 19

    def __init__(self, src):
        rules = {}
        objects = []
        for s in src.strip().split('\n'):
            if len(s) > 0:
                if s.startswith('{'):
                    data_clean = s.strip('{}')
                    pairs = data_clean.split(',')
                    dictionary = {}
                    for pair in pairs:
                        key, value = pair.split('=')
                        dictionary[key.strip()] = int(value.strip())
                    objects.append(dictionary)
                else:
                    key, conditions = s.split('{', 1)
                    conditions = conditions.strip('}')
                    condition_pairs = conditions.split(',')
                    condition_list = []
                    for condition in condition_pairs:
                        cond = condition.split(':')
                        if len(cond) == 1:
                            cond = ['True'] + cond
                        condition_list.append(cond)
                    rules[key] = condition_list
        return rules, objects

    def solve_part_1(self):
        end_set = {'A', 'R'}
        rules, objects = self.parse(src)
        ans = 0
        for obj in objects:
            val = sum(obj.values())
            now = "in"
            while True:
                for cond, nxt in rules[now]:
                    if eval(cond, obj):
                        now = nxt
                        break
                if now in end_set:
                    break
            if now == 'A':
                ans += val
        return ans

    def solve_part_2(self):
        rules, objects = self.parse(src)
        regex_pattern = r"(\w+)([><]=?)(\d+)"
        m, M = 1, 4000
        obj = {ch: [m, M] for ch in 'xmas'}

        def dfs(obj, now):
            for l, r in obj.values():
                if l > r:
                    return 0
            if now == 'A':
                val = 1
                for l, r in obj.values():
                    val *= (r - l + 1)
                return val
            elif now == 'R':
                return 0
            ans = 0
            for cond, nxt in rules[now]:
                if cond == 'True':
                    ans += dfs(obj, nxt)
                else:
                    var, op, num = re.findall(regex_pattern, cond)[0]
                    num = int(num)
                    l, r = obj[var]
                    if op == '>':
                        true_range = [max(num + 1, l), r]
                        false_range = [l, min(num, r)]
                    else:
                        true_range = [l, min(num - 1, r)]
                        false_range = [max(num, l), r]
                    obj[var] = true_range
                    obj2 = obj.copy()
                    ans += dfs(obj, nxt)
                    obj = obj2
                    obj[var] = false_range
            return ans

        return dfs(obj, 'in')


if __name__ == "__main__":
    sol = Solver2023Day19()
    src = get_data(Solver2023Day19.YEAR, Solver2023Day19.DAY)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
