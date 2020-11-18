import functools


def counter(f):
    f.depth = 0
    f.rdepth = 0
    f.ncalls = 0

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if wrapper.depth == 0:
            wrapper.rdepth = 0
            wrapper.ncalls = 0

        wrapper.depth += 1
        wrapper.ncalls += 1
        result = f(*args, **kwargs)
        wrapper.rdepth = max(wrapper.rdepth, wrapper.depth)
        wrapper.depth -= 1
        return result
    return wrapper
