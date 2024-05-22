from utils import Solver, get_data


class Solver2020Day21(Solver):
    YEAR = 2020
    DAY = 21

    def __init__(self, src):
        self.foods = []
        for s in src.strip().split('\n'):
            l, r = s.split('(contains')
            st1, st2 = set(l.strip().split()), set(r.strip(" )").split(", "))
            self.foods.append((st1, st2))
        self.ans1 = self.ans2 = None

    def run(self):
        allergen_set = set.union(*[food[1] for food in self.foods])
        info = {allergen: set.intersection(*[food[0] for food in self.foods if allergen in food[1]]) for allergen in
                allergen_set}
        match = dict()
        while len(info) > 0:
            new = {k: list(v)[0] for k, v in info.items() if len(v) == 1}
            match.update(new)
            info = {k: v - set(new.values()) for k, v in info.items() if len(v) > 1}
        self.ans1 = sum(len(food - set(match.values())) for food, _ in self.foods)
        self.ans2 = ",".join(v[1] for v in sorted(match.items()))

    def solve_part_1(self):
        return self.ans1

    def solve_part_2(self):
        return self.ans2


if __name__ == "__main__":
    src = get_data(Solver2020Day21.YEAR, Solver2020Day21.DAY)
    sol = Solver2020Day21(src)
    sol.run()
    print(sol.solve_part_1())
    print(sol.solve_part_2())
