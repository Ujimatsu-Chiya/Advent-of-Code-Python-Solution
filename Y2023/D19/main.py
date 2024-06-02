import re

from utils import Solver, get_data


class Solver2023Day19(Solver):
    YEAR = 2023
    DAY = 19

    def __init__(self, src):
        self.rules = {}
        self.objects = []
        rules_str, objects_str = src.strip().split('\n\n')
        for s in objects_str.split('\n'):
            data_clean = s.strip('{}')
            pairs = data_clean.split(',')
            dictionary = {}
            for pair in pairs:
                key, value = pair.split('=')
                dictionary[key.strip()] = int(value.strip())
            self.objects.append(dictionary)
        for s in rules_str.split('\n'):
            key, conditions = s.split('{', 1)
            conditions = conditions.strip('}')
            condition_pairs = conditions.split(',')
            condition_list = []
            for condition in condition_pairs:
                cond = condition.split(':')
                if len(cond) == 1:
                    cond = ['True'] + cond
                condition_list.append(cond)
            self.rules[key] = condition_list

    def solve_part_1(self):
        end_set = {'A', 'R'}
        ans = 0
        for obj in self.objects:
            val = sum(obj.values())
            now = "in"
            while True:
                for cond, nxt in self.rules[now]:
                    if eval(cond, obj):
                        now = nxt
                        break
                if now in end_set:
                    break
            if now == 'A':
                ans += val
        return ans

    def solve_part_2(self):
        pat = re.compile(r"(\w+)([><]=?)(\d+)")
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
            for cond, nxt in self.rules[now]:
                if cond == 'True':
                    ans += dfs(obj, nxt)
                else:
                    var, op, num = pat.findall(cond)[0]
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
    src = get_data(Solver2023Day19.YEAR, Solver2023Day19.DAY)
    sol = Solver2023Day19(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
