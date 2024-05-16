from functools import reduce
from itertools import combinations
from operator import mul

from utils import Solver, get_data


# class Solver2015Day24(Solver):
#     def __init__(self, src):
#         return list(map(int, src.strip().split()))
#
#     def solve_part_1(self):
#         # src = '''11 9       10 8 2  7 5 4 3 1'''
#         ls = sorted(self.parse(src), reverse=True)
#         avg = sum(ls) // 3
#         n = len(ls)
#         vis = [False for _ in range(n)]
#
#         def partition_half(a, v):
#             f = [False for _ in range(v + 1)]
#             f[0] = True
#             for x in a:
#                 for i in range(v, x - 1, -1):
#                     f[i] |= f[i - x]
#             return f[v]
#
#         ans_len, ans_qe = n + 1, 0
#
#         def dfs(f, pre_len, pre_qe, pre_sum):
#             nonlocal ans_len, ans_qe
#             if pre_sum > avg or pre_len > ans_len or pre_len == ans_len and pre_qe >= ans_qe:
#                 return
#             if f == len(ls):
#                 if pre_sum == avg and partition_half([ls[i] for i in range(n) if not vis[i]], avg):
#                     ans_len = pre_len
#                     ans_qe = pre_qe
#                 return
#             vis[f] = True
#             dfs(f + 1, pre_len + 1, pre_qe * ls[f], pre_sum + ls[f])
#             vis[f] = False
#             dfs(f + 1, pre_len, pre_qe, pre_sum)
#
#         dfs(0, 0, 1, 0)
#         return ans_qe
#
#     def solve_part_2(self):
#         def ok(ls):
#             avg = sum(ls) // 3
#             n = len(ls)
#
#             def partition_half(a, v):
#                 f = [False for _ in range(v + 1)]
#                 f[0] = True
#                 for x in a:
#                     for i in range(v, x - 1, -1):
#                         f[i] |= f[i - x]
#                 return f[v]
#
#             def dfs(f, pre_sum):
#                 if pre_sum > avg:
#                     return False
#                 if f == len(ls):
#                     if pre_sum == avg and partition_half([ls[i] for i in range(n) if not vis[i]], avg):
#                         nonlocal ok
#                         return True
#                     return
#                 if dfs(f + 1, pre_sum + ls[f]):
#                     return True
#                 if dfs(f + 1, pre_sum):
#                     return True
#                 return False
#
#             return dfs(0, 0)
#
#         # src = '''11 9       10 8 2  7 5 4 3 1'''
#
#         ls = sorted(self.parse(src), reverse=True)
#         print(ls)
#         avg = sum(ls) // 4
#         n = len(ls)
#         vis = [False for _ in range(n)]
#         ans_len, ans_qe = n + 1, 0
#
#         def dfs(f, pre_len, pre_qe, pre_sum):
#             nonlocal ans_len, ans_qe
#             if pre_sum > avg or pre_len > ans_len or pre_len == ans_len and pre_qe >= ans_qe:
#                 return
#             if f == len(ls):
#                 if pre_sum == avg and ok([ls[i] for i in range(n) if not vis[i]]):
#                     ans_len = pre_len
#                     ans_qe = pre_qe
#                 return
#             vis[f] = True
#             dfs(f + 1, pre_len + 1, pre_qe * ls[f], pre_sum + ls[f])
#             vis[f] = False
#             dfs(f + 1, pre_len, pre_qe, pre_sum)
#         dfs(0,0,1,0)
#         return ans_qe


class Solver2015Day24(Solver):
    YEAR = 2015
    DAY = 24

    def __init__(self, src):
        self.a = list(map(int, src.strip().split()))

    def _solve(self, ls, k):
        avg = sum(ls) // k
        for i in range(len(ls)):
            qes = [reduce(mul, c) for c in combinations(ls, i) if sum(c) == avg]
            if qes:
                return min(qes)

    def solve_part_1(self):
        return self._solve(self.a, 3)

    def solve_part_2(self):
        return self._solve(self.a, 4)


if __name__ == "__main__":
    src = get_data(Solver2015Day24.YEAR, Solver2015Day24.DAY)
    sol = Solver2015Day24(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
