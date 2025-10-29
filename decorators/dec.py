import time

def logger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Running '{func.__name__}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Finished '{func.__name__}' in {end - start:.2f} sec")
        return result
    return wrapper

@logger  #decorator
def fun():
    time.sleep(2)
    print("Work done!")
    
fun()
