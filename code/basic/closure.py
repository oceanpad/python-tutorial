def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

t = lazy_sum(1,3,5)
print(t())

t1 = lazy_sum(1,3,5)
t2 = lazy_sum(1,3,5)
print(t1 == t2)
