def f(x):
    return x*x

def test(x, y, f = f):
    return (f(x) + f(y))

print(test(88, 4, f))
