import time


def tim(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        result = func(*args, **kwargs)
        print(f"fin du temps {time.time()-debut}s")
        return result

    return wrapper


@tim
def changer():
    return 34 + 6


changer()
