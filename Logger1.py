from datetime import datetime


def log_decor(old_function):
    def new_function(*args, **kwargs):
        obg = old_function()
        info = dict()
        info['record'] = datetime.utcnow()
        info['args'] = args
        info['kwargs'] = kwargs
        info['resault'] = obg
        info['name'] = old_function.__name__

        with open('algo.txt', 'w', encoding = 'utf-8') as file:
            for keys,values in info.items():
                file.write(f'{keys} : {values}\n')

        return info

    return new_function

@log_decor
def foo():
    return 'hi'

print(foo())




