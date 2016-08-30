'''
# build in Functions
print(abs(100))
print(abs(-20))
print(max(-20, 20, 30, 40))
print(int('-20'))
print(str(1.234))
print(bool(''))
print(bool(12))
#assign Functions name
a = abs
print(a(12))
'''
# define function
def myAbs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x

# null function(Use pass)
def nop():
    pass

def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5))
