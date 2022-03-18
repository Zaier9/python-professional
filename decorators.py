# Esta es una funcion decorador
from textwrap import wrap


def decorator(func):
    def wrapper():
        return func() + ' decorada.'
    return wrapper

# Decorando una funcion
def my_func1():
    text = 'Esta es la primer funcion'
    return text

texto = decorator(my_func1)
print(texto()) # Output: Esta es la primer funcion decorada.

# Decorando otra funcion con sugar syntax
@decorator
def my_func2():
    text = 'Esta es la segunda funcion'
    return text

print(my_func2()) #Output: Esta es la segunda funcion decorada.