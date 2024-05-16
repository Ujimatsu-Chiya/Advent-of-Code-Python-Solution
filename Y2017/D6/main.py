from utils import Solver, get_data


class Solver2017Day6(Solver):
    YEAR = 2017
    DAY = 6

    def __init__(self, src):
        self.a= list(map(int, src.strip().split()))

    def solve_part_1(self):
        a = self.a
        n = len(a)
        st = set(tuple(a))
        cnt = 0
        while True:
            cnt += 1
            p = a.index(max(a))
            x = a[p]
            a[p] = 0
            q, r = divmod(x, n)
            for i in range(n):
                a[(p + i + 1) % n] += q + int(i < r)
            t = tuple(a)
            if t in st:
                break
            else:
                st.add(t)
        return cnt

    def solve_part_2(self):
        a = self.a
        n = len(a)
        mp = {tuple(a): 0}
        cnt = 0
        while True:
            cnt += 1
            p = a.index(max(a))
            x = a[p]
            a[p] = 0
            q, r = divmod(x, n)
            for i in range(n):
                a[(p + i + 1) % n] += q + int(i < r)
            t = tuple(a)
            if t in mp.keys():
                return cnt - mp[t]
            else:
                mp[t] = cnt


if __name__ == "__main__":
    src = get_data(Solver2017Day6.YEAR, Solver2017Day6.DAY)
    sol = Solver2017Day6(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
