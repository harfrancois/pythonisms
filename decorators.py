from functools import wraps
from time import sleep

def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_val_from_undecorated_function = func(*args, **kwargs)
        emphasized = return_val_from_undecorated_function.upper() + "!!!"
        return emphasized
    return wrapper

def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Oh Sure, "{orig_val}" sounds great'

    return wrapper


def proclaim(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return "I do say, " + orig_val
    return wrapper

def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(6.66)
        return func(*args, **kwargs)
    return wrapper


@procrastinate
@proclaim
def say(txt):
    return txt

@sarcastic_decorator
@emphasize
def restaurant_suggestion(cuisine):
    return cuisine

if __name__ == "__main__":
    print(say('Im the best.'))
    print(restaurant_suggestion("Chinese"))