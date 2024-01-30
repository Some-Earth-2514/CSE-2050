# this function
def foo(arg1, arg2, arg3, defarg1="hello", defarg2="goodbye"):
    """DOC STRING that describes what the function does"""
    print(arg1, defarg1)
    return arg2


x = foo(1, 2, 3)

print(f"x = {x}")
help(foo)


def unique_string(word):
    word_set = set(word)
    is_unique = len(word_set) == len(word)
    return is_unique


print(unique_string(word='hello'))
