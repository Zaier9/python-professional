def my_gen():
    print('Hello World!')
    n = 0
    yield n

    print('Hello Heaven!')
    n = 1
    yield n

    print('Hello Hell!')
    n = 2
    yield n

a = my_gen()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
