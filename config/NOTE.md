# ConfigParser
## Purpose
- It's usefult to read config files.
- Convenient to read .ini files

## Notes
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
- Common using functions
    - config.`read`
    - config.`sections`


### reference
1. http://zetcode.com/python/configparser/
2. https://www.amazon.in/Python-Cookbook-Recipes-Mastering-ebook/dp/B00DQV4GGY
3. https://docs.python.org/3/library/configparser.html#supported-ini-file-structure