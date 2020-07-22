from _datetime import datetime


def log_decor(old_function):
    def new_function(*args, **kwargs):
        obg = old_function(*args, **kwargs)
        info = dict()
        info['record'] = datetime.utcnow()
        info['args'] = args
        info['kwargs'] = kwargs
        info['resault'] = obg
        info['name'] = old_function.__name__

        with open('algo.txt', 'w', encoding = 'utf-8') as file:
            for keys,values in info.items():
                file.write(f'{keys} : {values}\n')

        return obg

    return new_function

@log_decor
def foo(a, b):
    return a+b

a = 13

b = 12

print(foo(a, b))
