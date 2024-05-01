import os

import gmpy2
import requests
import sympy


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
    return [[mp[i][j] for i in range(len(mp))] for j in range(len(mp[0]))]


def transpose_str(mp):
    return ["".join(mp[i][j] for i in range(len(mp))) for j in range(len(mp[0]))]


def rotate(mp):
    return transpose(mp[::-1])


def rotate_str(mp):
    return transpose_str(mp[::-1])


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


def get_data(year: int, day: int) -> str:
    root = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(root, '{}/{}/input.txt'.format(year, day))
    if not os.path.exists(input_path):
        session = open(os.path.join(root, '.session')).read().strip()
        input_url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
        cookies = {'session': session}
        src = requests.get(input_url, cookies=cookies).text
        with open(input_path, 'w+') as fp:
            fp.write(src)
    return open(input_path).read()


if __name__ == "__main__":
    # 获取当前脚本文件的绝对路径
    current_path = os.path.abspath(__file__)

    # 获取当前脚本文件所在的目录路径
    current_dir = os.path.dirname(current_path)
    print(current_dir)
    # 获取项目根目录
    project_dir = os.path.dirname(current_dir)
    print(project_dir)
