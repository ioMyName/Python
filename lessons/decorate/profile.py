from functools import wraps


def profiled(func):
    @wraps(func)
    def inner(*args, **kwargs):
        inner.ncalls += 1
        return func(*args, **kwargs)

    inner.ncalls = 0
    return inner


@profiled
def identity(x):
    return x


identity(42)
identity(42)
identity(42)
print(identity.ncalls)
print(identity.ncalls)
print(identity.ncalls)