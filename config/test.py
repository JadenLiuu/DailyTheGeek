import configparser
from utils.decorators import print_function_name

CONFIG = './config/config.ini'
CONFIG_ADD = './config/config_add.ini'


@print_function_name
def test_bool():
    cf = configparser.ConfigParser()

    # We initiate the ConfigParser and read the file with read().
    cf.read(CONFIG)
    print(cf.sections())  # ['BOOL_TEST']

    if cf.has_section('BOOL_TEST'):
        for opt in cf['BOOL_TEST']._options():
            print(f'\n{opt}:', )
            print(cf['BOOL_TEST'][opt])
            # showing case-insensitive of the keys
            print(cf.getboolean('BOOL_TEST', opt))
            print(cf.getboolean('BOOL_TEST', opt.upper()))


@print_function_name
def test_stringlike_config():
    # appear after python 3.2
    cfg_data = '''
    [mysql]
    host = localhost
    user = user7
    passwd = s$cret
    db = ydb
    '''
    cf = configparser.ConfigParser()
    cf.read_string(cfg_data)
    print('cf sections: ', cf.sections())


@print_function_name
def test_dict_config():
    cfg_data = {
        'mysql': {
              'host': 'localhost',
              'user': 'user7',
              'passwd': 's$cret',
              'db': 'ydb'
        }
    }
    cf = configparser.ConfigParser()
    cf.read_dict(cfg_data)
    print(cf.sections())


@print_function_name
def test_prefix():
    cf = configparser.ConfigParser()
    cf.read(CONFIG)
    section = cf['PREFIX']
    print(section.get('prefix'))


@print_function_name
def test_write_out():
    cf = configparser.ConfigParser()
    cf.read(CONFIG)
    cf['PREFIX']['name'] = 'Lala'
    if not cf.has_section('ADD_OUT'):
        cf.add_section('ADD_OUT')
        cf['ADD_OUT']['name'] = 'Jaden'
        with open(CONFIG_ADD, 'w') as cfile:
            cf.write(cfile)


if __name__ == '__main__':
    test_bool()
    test_stringlike_config()
    test_dict_config()
    test_prefix()
    test_write_out()
