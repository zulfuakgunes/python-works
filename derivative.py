import math


def gradient(func):
    import functools
    @functools.wraps(func)
    def wrapper(x):
        h = 0.0000001
        dfx = (func(x+h)-func(x))/h
        return f'{dfx:.5f}'
    return wrapper


""" Testing """
@gradient
def f(x): return math.log(x)


@gradient
def g(a): return a**2+5*a


sonuc = f(5)
sonuc2 = g(3)
print(sonuc, sonuc2)
