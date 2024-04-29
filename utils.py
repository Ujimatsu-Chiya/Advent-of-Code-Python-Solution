import sympy,gmpy2


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dis(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __xor__(self, other):
        return self.x * other.y - self.y * other.x

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __len__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solver:
    def parse(self, src):
        raise NotImplementedError()

    def solve_part_1(self, src):
        raise NotImplementedError()

    def solve_part_2(self, src):
        raise NotImplementedError()


def transpose(mp):
    return ["".join(mp[i][j] for i in range(len(mp))) for j in range(len(mp[0]))]


def rotate(mp):
    return transpose(list(reversed(mp)))

def is_prime(n):
    return gmpy2.is_prime(n)
def factorization(n):
    ls = list(sympy.factorint(n).items())
    ls.sort()
    return ls


def divisors_sigma(n, k=None):
    ls = factorization(n)
    ans = 1
    if k is None:
        for p, e in ls:
            ans *= (p ** (e + 1) - 1) // (p - 1)
    elif k == 0:
        for p, e in ls:
            ans *= e + 1
    else:
        for p, e in ls:
            t = p ** k
            ans *= (t ** (e + 1) - 1) // (t - 1)
    return ans


# 使用示例
if __name__ == "__main__":
    p1 = Point(3, 4)
