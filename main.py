def simple_count(s):
    return len(s)  # Correctly returns the length of the string


def random_function():
    import random
    if random.random() < 0.001:
        return True
    else:
        return False


def complex_function():
    if random_function():
        return 'behaviour 1'
    else:
        return 'behaviour 2'
