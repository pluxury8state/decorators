from datetime import datetime


def new_logger(file_path):
    def _log_decor(old_function):
        def new_function(*args, **kwargs):
            obg = old_function()
            info = dict()
            info['record'] = datetime.utcnow()
            info['args'] = args
            info['kwargs'] = kwargs
            info['resault'] = obg
            info['name'] = old_function.__name__


            with open(file_path, 'w', encoding='utf-8') as file:
                for keys, values in info.items():
                    file.write(f'{keys} : {values}\n')

        return new_function
    return _log_decor


@new_logger('asdasd.txt')
def func():
    return 'hi'

func('arg',kwarg = 8)