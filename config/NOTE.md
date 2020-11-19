# ConfigParser
## Purpose
- It's usefult to read config files.
- Convenient to read .ini files

## Let's start
- take all of the files in each project as a module.
- This notes is the project of `config`
    ```sh
    python3 -m config.test
    ```

## Notes
### Overall
- section are tagged with `[]`; each contains pairs of `key:value` (or `key=value`)
    - we call the `key:value` pair `option` here.
- The names (`key`) are case-insensitive; But the `section` is case-sensitive!!
- They are parsed at the sametime. ie., They are not executed in a top-down manner.
    ```python
    [installation]
    library=%(prefix)s/lib
    include=%(prefix)s/include
    bin=%(prefix)s/bin
    prefix=/usr/local
    ```
    - It's Okay that `prefix` is assigned latter. The **order doesn't matter**
- Usually we use string type in files, but `ConfigParser` support types (int, float, bool)
- config for `bool`
    - most interesting part!
    - because 'any_string' is True in such case, `ConfigParser` provides the `getboolean` function.
    - Config could be specified with: `yes`/`no`, `on`/`off`, `true`/`false` and `1`/`0`
        - see `test_bool` function in the `test.py`
### Common using functions
- config.`read`(`file`)
    - To read the config `file`.
- config.`sections`()
    - Directly get all the `sections` in the config file.
- config.`has_section`(`section`)
    - Check if we have `section` in the config.

### Read from string
- Maybe you would want to use string config defined in your python script.
    => Use `read_string` here.
    1. define a string just like the `.ini` files.
    2. use `read_string` to set the config parser.
- see `test_stringlike_config` function in the `test.py`

### Dictionary works too
- Use `read_dict` in this case.
    ```Python
    cfg_data = {
        'mysql': {'host': 'localhost', 'user': 'user7',
                'passwd': 's$cret', 'db': 'ydb'}
    }
    ```
- see `test_dict_config` function in the `test.py`
### ini File
- ConfigParser allows to use interpolation in the configuration file. It uses the `%()s` syntax.
- see `test_prefix` function in the `test.py`

### Write the config out
- You cannot add an existing section.
- In contrast, adding an existing option to one existed section will not raise error.
    - Option is presented as a `dict`, it's okay to modify it.
- Write out your config simpy via
    ```python
    with open(CONFIG_ADD, 'w') as cfile:
        cf.write(cfile)
    ```
- see `test_write_out` function in the `test.py`


### reference
1. http://zetcode.com/python/configparser/
2. https://www.amazon.in/Python-Cookbook-Recipes-Mastering-ebook/dp/B00DQV4GGY
3. https://docs.python.org/3/library/configparser.html#supported-ini-file-structure