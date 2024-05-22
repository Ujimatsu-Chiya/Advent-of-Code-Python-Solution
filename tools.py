import hashlib
from collections import defaultdict, deque
from functools import reduce
import operator
from typing import NamedTuple

import gmpy2
import sympy
import numpy as np


class Point(NamedTuple('Point', [('x', int), ('y', int)])):

    def dis(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __xor__(self, other):
        return self.x * other.y - self.y * other.x

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __truediv__(self, scalar):
        return Point(self.x / scalar, self.y / scalar)

    def __floordiv__(self, scalar):
        return Point(self.x // scalar, self.y // scalar)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def manhattan_dis(self):
        return abs(self.x) + abs(self.y)

    def neighbor4(self):
        return [self + p for p in self.dirs4]

    def quadrant(self):
        if self.x > 0 and self.y >= 0:
            return 1
        elif self.x <= 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y <= 0:
            return 3
        else:
            return 4


Point.dirs4 = [Point(0, 1), Point(0, -1), Point(-1, 0), Point(1, 0)]


def transpose(mp):
    return [[mp[i][j] for i in range(len(mp))] for j in range(len(mp[0]))]


def transpose_str(mp):
    return ["".join(mp[i][j] for i in range(len(mp))) for j in range(len(mp[0]))]


def rotate(mp):
    return transpose(mp[::-1])


def rotate_str(mp):
    return transpose_str(mp[::-1])


is_prime = gmpy2.is_prime


def factorization(n):
    return sorted(sympy.factorint(n).items())


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


mod_inverse = sympy.mod_inverse

sgn = np.sign


def CRT(a_list, m_list):
    M = reduce(operator.mul, m_list)
    ans = 0
    for a, m in zip(a_list, m_list):
        mi = M // m
        t = mod_inverse(mi, m)
        ans += mi * t * a
    return ans % M


def md5_digest(s):
    md5 = hashlib.md5(s.encode())
    return md5.hexdigest()


def sorted_str(s):
    return "".join((lambda x: (x.sort(), x)[1])(list(s)))


class IntCodeComputer:
    jmp = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]

    def __init__(self, program: list, input_array=[]):
        self.ops = defaultdict(int)
        self.sz = len(program)
        for i, x in enumerate(program):
            self.ops[i] = x
        self.pc = 0
        self.input = deque(input_array)
        self.output = deque()
        self.halt = False
        self.base = 0

    def __hash__(self):
        return hash(tuple(sorted(self.ops.items())))

    def get_pos(self, i, mod):
        return self.ops[i] if mod == 0 else i if mod == 1 else self.base + self.ops[i]

    def parse(self, opcode):
        s = "{:05}".format(opcode)
        return tuple(map(int, [s[3:], s[2], s[1], s[0]]))

    def run(self):
        while not self.halt:
            op, *mods = self.parse(self.ops[self.pc])
            idx = [self.get_pos(self.pc + i + 1, mods[i]) for i in range(3)]
            match op:
                case 1:
                    self.ops[idx[2]] = self.ops[idx[0]] + self.ops[idx[1]]
                case 2:
                    self.ops[idx[2]] = self.ops[idx[0]] * self.ops[idx[1]]
                case 3:
                    if len(self.input) == 0:
                        break
                    self.ops[idx[0]] = self.input.popleft()
                case 4:
                    self.output.append(self.ops[idx[0]])
                case 5:
                    if self.ops[idx[0]] != 0:
                        self.pc = self.ops[idx[1]]
                        continue
                case 6:
                    if self.ops[idx[0]] == 0:
                        self.pc = self.ops[idx[1]]
                        continue
                case 7:
                    self.ops[idx[2]] = int(self.ops[idx[0]] < self.ops[idx[1]])
                case 8:
                    self.ops[idx[2]] = int(self.ops[idx[0]] == self.ops[idx[1]])
                case 9:
                    self.base += self.ops[idx[0]]
                case 99:
                    self.halt = True
                    break
                case _:
                    assert False
            self.pc += self.jmp[op]

    def add_input(self, x):
        self.input.append(x)

    def add_list_input(self, a: list):
        self.input += a

    def add_ascii_input(self, s):
        self.input += [ord(ch) for ch in s]

    def get_output(self):
        if len(self.output) == 0:
            self.run()
        return self.output.popleft()

    def get_all_output(self):
        if len(self.output) == 0:
            self.run()
        t = list(self.output)
        self.output = deque()
        return t

    def get_ascii_output(self):
        return "".join(chr(x) for x in self.get_all_output())
