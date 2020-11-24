# Threading — Thread-based parallelism

## Comparison
- Multithreading is concurrent and is used for IO-bound tasks
- Multiprocessing achieves true parallelism and is used for CPU-bound tasks

## Discussion
- suited for I/O handling
- handling concurrent execution in code that performs
blocking operations (e.g., waiting for I/O, waiting for results from a database, etc.).
- Not suit for **computationally intensive** works!!

## Construction
```python
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```
- `group`: developed for future extension
- `target`: callable object
- `name`: name of this thread
- `args` & `kwargs`: parameters to be passed into your target.

## Run your threads
- use `start`, it invokes `run`. It raise stop exception if the `start` function is called twice (or above).
- we asked `3, 5, 2` seconds to sleep via threading, the running result of this program is:
    ```
    real    0m 5.08s
    user    0m 0.03s
    sys     0m 0.01s
    ```
- use `join` to stop your threds

## Other useful functions
- `t` as an instance of threading.Thread; `threading` as the moudle name.
- `t.is_alive()`
- `t.getName()`
- `threading.active_count()`: equal to the length of `threading.enumerate()`
- `threading.enumerate()` : get the list of currently alive threads. including main thread!
- There are other useful APIs, see **APIs** below.

## APIs
https://docs.python.org/3/library/threading.html

## Reference
1. https://www.amazon.in/Python-Cookbook-Recipes-Mastering-ebook/dp/B00DQV4GGY
2. https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/
