from utils import Solver, get_data


class Solver2016Day21(Solver):
    YEAR = 2016
    DAY = 21

    def __init__(self, src):
        ls = src.strip().split('\n')
        ops = []
        for s in ls:
            t = s.split()
            match " ".join(t[:2]):
                case "swap position":
                    ops.append(["swap position", int(t[2]), int(t[5])])
                case "swap letter":
                    ops.append(["swap letter", t[2], t[5]])
                case "rotate left":
                    ops.append(["rotate", int(t[2])])
                case "rotate right":
                    ops.append(["rotate", -int(t[2])])
                case "rotate based":
                    ops.append(["rotate based", t[6]])
                case "reverse positions":
                    ops.append(["reverse", int(t[2]), int(t[4])])
                case "move position":
                    ops.append(["move", int(t[2]), int(t[5])])
        self.ops = ops

    def _rotate(self, a, k):
        k %= len(a)
        return a[k:] + a[:k]

    def _swap(self, a, i, j):
        a[i], a[j] = a[j], a[i]
        return a

    def _move(self, a, i, j):
        ch, a = a[i], a[:i] + a[i + 1:]
        return a[:j] + [ch] + a[j:]

    def _revesse(self, a, i, j):
        i, j = sorted([i, j])
        return a[:i] + a[i:j + 1][::-1] + a[j + 1:]

    def _rotate_based(self, a, ch):
        idx = a.index(ch) + 1
        if idx >= 5:
            idx += 1
        return self._rotate(a, -idx)

    def solve_part_1(self):
        a = list("abcdefgh")
        for o in self.ops:
            if o[0] == "rotate":
                a = self._rotate(a, o[1])
            elif o[0] == 'swap position':
                a = self._swap(a, o[1], o[2])
            elif o[0] == 'swap letter':
                a = self._swap(a, a.index(o[1]), a.index(o[2]))
            elif o[0] == 'reverse':
                a = self._revesse(a, o[1], o[2])
            elif o[0] == 'rotate based':
                a = self._rotate_based(a, o[1])
            elif o[0] == 'move':
                a = self._move(a, o[1], o[2])
            else:
                assert False
        return "".join(a)

    def solve_part_2(self):
        a = list("fbgdceah")
        for o in self.ops[::-1]:
            if o[0] == "rotate":
                a = self._rotate(a, -o[1])
            elif o[0] == 'swap position':
                a = self._swap(a, o[1], o[2])
            elif o[0] == 'swap letter':
                a = self._swap(a, a.index(o[1]), a.index(o[2]))
            elif o[0] == 'reverse':
                a = self._revesse(a, o[1], o[2])
            elif o[0] == 'rotate based':
                for i in range(len(a)):
                    b = self._rotate(a, i)
                    if self._rotate_based(b, o[1]) == a:
                        a = b
                        break
            elif o[0] == 'move':
                a = self._move(a, o[2], o[1])
            else:
                assert False
        return "".join(a)


if __name__ == "__main__":
    src = get_data(Solver2016Day21.YEAR, Solver2016Day21.DAY)
    sol = Solver2016Day21(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
