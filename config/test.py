import configparser

CONFIG = './config.ini'


def test_bool():
    cf = configparser.ConfigParser()
    cf.read(CONFIG)
    print(cf.sections())  # ['BOOL_TEST']

    if cf.has_section('BOOL_TEST'):
        for opt in cf['BOOL_TEST']._options():
            print(f'\n{opt}:', )
            print(cf['BOOL_TEST'][opt])
            print(cf.getboolean('BOOL_TEST', opt))
            print(cf.getboolean('BOOL_TEST', opt.upper()))


if __name__ == '__main__':
    test_bool()
