import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result  = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def Example_func(n):
    time.sleep(n)
    print(f"hold for {n} sec. then successfully Execute")

Example_func(2)