def howlong(function):
    import time

    def wrapper(*args, **kwargs):
        tic = time.time()
        function(*args, **kwargs)
        toc = time.time()
        f = f'{function.__name__} function took {toc-tic:.8f}'
        print(f)
        return function(*args, **kwargs)
    return wrapper
    
    
    """ Test """
@howlong
def multiply():
    import numpy as np
    m1 = np.random.rand(500, 100)
    m2 = np.random.rand(100, 2000)
    y = np.dot(m1, m2)
    return y


print(multiply())
