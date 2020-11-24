from utils.decorators import print_function_name
import time
import threading


class Runner:
    def __init__(self, name, running_time):
        print(f'Runner: {name}')
        time.sleep(running_time)


@print_function_name
def test():
    # threading.setprofile(Runner)
    t1 = threading.Thread(target=Runner, args=('Jaden', 3), name='jaden')
    t2 = threading.Thread(target=Runner, args=('Frank', 5), name='frank')
    t3 = threading.Thread(target=Runner, args=('Lulu', 2), name='lulu')

    tlist = [t1, t2, t3]

    for thread in tlist:
        thread.start()

    while threading.active_count() > 1:
        # print(threading.enumerate())
        time.sleep(0.5)
        print(threading.active_count())
        for thread in tlist:
            t_name = thread.getName()
            aliveness = thread.is_alive()
            print(f'{t_name} is alive? {aliveness}')

    for thread in tlist:
        thread.join()

    print('Main thread ended.')


if __name__ == '__main__':
    test()
