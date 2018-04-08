import time

cache = {}


def blueis(func):
    def cached():
        start = time.time()
        name = func.__name__
        if name in cache:
            print('I spent {}s'.format(time.time() - start))
            print(cache[name])
        else:
            cache[name] = func()

    return cached


def get_sql():
    time.sleep(1)
    return [1, 2, 3]


@blueis
def get_data():
    start = time.time()
    data = get_sql()
    print('I spent {}s'.format(time.time() - start))
    print(data)
    return data


if __name__ == '__main__':
    print('cache', cache)
    get_data()

    print('--- --- ---')

    print('cache', cache)
    get_data()
