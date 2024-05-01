import json

from utils import Solver, get_data


class Solver2015Day12(Solver):
    YEAR = 2015
    DAY = 12


    def parse(self, src):
        return json.loads(src.strip())

    def solve_part_1(self, src):
        mp = self.parse(src)

        def dfs(obj):
            ans = []
            if isinstance(obj, int):
                ans.append(obj)
            elif isinstance(obj, list):
                for obj2 in obj:
                    ans += dfs(obj2)
            elif isinstance(obj, dict):
                for v in obj.values():
                    ans += dfs(v)
            return ans

        return sum(dfs(mp))

    def solve_part_2(self, src):
        mp = self.parse(src)

        def dfs(obj):
            ans = []
            if isinstance(obj, int):
                ans.append(obj)
            elif isinstance(obj, list):
                for obj2 in obj:
                    ans += dfs(obj2)
            elif isinstance(obj, dict):
                if 'red' in obj.values():
                    return []
                for v in obj.values():
                    ans += dfs(v)
            return ans

        return sum(dfs(mp))


if __name__ == "__main__":
    sol = Solver2015Day12()
    src = get_data(Solver2015Day12.YEAR, Solver2015Day12.DAY)
    print(sol.solve_part_1(src))
    print(sol.solve_part_2(src))
