def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log #put @log here is main that "now = log(now)"
def now():
    print('2015-3-25')

now()
