def pretty_print(func):
    def wrapper_function(*args, **kwargs):
        print()
        print("-----------------------------")
        result = func(*args, **kwargs)
        return result
    return wrapper_function
