# The decorator to print the functions
def print_function_name(f):
    def wrap():
        print('='*20)
        print(' '*3, f.__name__)
        print('='*20)
        f()
    return wrap
