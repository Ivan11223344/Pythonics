def generator():
    yield 1  # возвращает выполненные потоки программы
    yield 2
    yield 3


g = gen()
next(g)
next(g)
