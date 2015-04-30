import asyncio

def foo():
    item = yield
    yield from asyncio.sleep(2)
    yield item*2


if __name__ == '__main__':
    a = foo()
    next(a)
    print(a.send(42))