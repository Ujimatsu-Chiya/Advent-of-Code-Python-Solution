from utils import Solver, get_data


class Solver2019Day16(Solver):
    YEAR = 2019
    DAY = 16

    def __init__(self, src):
        self.a = [int(ch) for ch in src.strip()]

    def solve_part_1(self):
        a = self.a
        n = len(a)
        p = [0, 1, 0, -1]
        p_list = []
        for i in range(1, n + 1):
            q_list = []
            res = n - i + 1
            q_list.append(i - 1)
            k, m = divmod(res, i)
            q_list += [i] * k + [m]
            p_list.append(q_list)

        def trans(a):
            s = [0]
            for x in a:
                s.append(s[-1] + x)
            b = []
            for pat in p_list:
                pos = val = 0
                for i in range(len(pat)):
                    val += p[i % len(p)] * (s[pos + pat[i]] - s[pos])
                    pos += pat[i]
                b.append(abs(val) % 10)
                assert pos == n
            return b

        M = 100
        for i in range(M):
            a = trans(a)
        return "".join(str(x) for x in a[:8])

    def solve_part_2(self):
        a = self.a * 10000
        n = len(a)
        o = int("".join(str(x) for x in a[:7]))
        assert o + o >= len(a) - 1
        for i in range(100):
            s = sum(a[o:])
            for j in range(o, n):
                t = s
                s -= a[j]
                a[j] = abs(t) % 10
        return "".join(str(x) for x in a[o:o + 8])


if __name__ == "__main__":
    src = get_data(Solver2019Day16.YEAR, Solver2019Day16.DAY)
    sol = Solver2019Day16(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
