import heapq
from timeit import Timer

seq = [100, 2, 400, 500, 400]

def a(seq):
    """returns [(3, 500), (2, 400)]"""
    return heapq.nlargest(2, enumerate(seq), key=lambda x: x[1])

def b(seq):
    """returns [3, 2]"""
    return map(seq.index, heapq.nlargest(2, seq))

def c(seq):
    """returns [(500, 3), (400, 2)]"""
    map(lambda n: (n, seq.index(n)), heapq.nlargest(2, seq))

if __name__ == '__main__':
    _a = Timer("a(seq)", "from __main__ import a, seq")
    _b = Timer("b(seq)", "from __main__ import b, seq")
    _c = Timer("c(seq)", "from __main__ import c, seq") 

    loops = 1000000

    print (_a.timeit(number=loops))
    print (_b.timeit(number=loops))
    print (_c.timeit(number=loops))

