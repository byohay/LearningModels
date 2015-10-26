import time

__author__ = 'yben_000'


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %f seconds' % (f.func_name, (time2-time1))
        return ret
    return wrap
