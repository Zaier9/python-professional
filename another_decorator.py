from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_tme = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_tme
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos.")
    return wrapper


@execution_time
def random_func():
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b


random_func()
suma(2,2)

