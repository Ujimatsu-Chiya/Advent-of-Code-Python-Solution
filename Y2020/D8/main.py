from utils import Solver, get_data


class Solver2020Day8(Solver):
    YEAR = 2020
    DAY = 8

    def __init__(self, src):
        self.ops = [list(map(lambda t: int(t) if t[-1].isdigit() else t, s.split())) for s in src.strip().split('\n')]

    def _run(self, ops):
        val = 0
        pos = 0
        st = set()
        while 0 <= pos < len(ops):
            if pos in st:
                return False, val
            st.add(pos)
            ins = ops[pos]
            if ins[0] == 'acc':
                val += ins[1]
                pos += 1
            elif ins[0] == 'jmp':
                pos += ins[1]
            else:
                pos += 1
        return True, val

    def solve_part_1(self):
        return self._run(self.ops)[1]

    def solve_part_2(self):
        for i in range(len(self.ops)):
            if self.ops[i][0] in ["nop", "jmp"]:
                self.ops[i][0] = "nop" if self.ops[i][0] == "jmp" else "jmp"
                flag, val = self._run(self.ops)
                if flag:
                    return val
                self.ops[i][0] = "nop" if self.ops[i][0] == "jmp" else "jmp"


if __name__ == "__main__":
    src = get_data(Solver2020Day8.YEAR, Solver2020Day8.DAY)
    sol = Solver2020Day8(src)
    print(sol.solve_part_1())
    print(sol.solve_part_2())
