def log_writer(file_name):
    def log_errors(func):
        def surrogate(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as exc:
                with open(file_name, mode='a', encoding='utf8') as write_file_wrong:
                    content_log = f'{func.__name__} -> {type(exc).__name__}, {args}, {kwargs}, {exc}\n'
                    write_file_wrong.write(content_log)
                raise

        return surrogate

    return log_errors


@log_writer('function_errors_one.log')
def perky(param):
    return param / 0


@log_writer('function_errors_second.log')
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)
