what methods must an object implement to support the context
management protocol in Python? `.__enter__()` and `.__exit__()`

--------------------------------------------------------------------------------
wrap a threading.Lock object within a with statement?  To
automatically acquire and release a lock

--------------------------------------------------------------------------------
When you need to work with asynchronous context managers in
Python, you use the `async with` statement.  This statement is
similar to the regular with statement but is designed for use in
asynchronous code.  Asynchronous context managers implement the
special methods `.__aenter__()` and `.__aexit__()`, which allow
the context manager to suspend execution during their enter and
exit phases.

--------------------------------------------------------------------------------
In a context manager, if you want to handle an exception and
prevent it from propagating, you should return a truthy value,
such as True, from `.__exit__()`.  This tells Python that the
exception has been dealt with and execution can continue
normally.  Here’s an example where `.__exit__()` handles an
IndexError:

```python
class HelloContextManager:
    # ...
    def __exit__(self, exc_type, exc_value, exc_tb):
        if isinstance(exc_value, IndexError):
            print(f"An exception occurred: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True
```

If `.__exit__()` returns `True`, then you can consider the
exception handled, so the program continues execution after the
with block.  If it returns `False` or `None`, then Python will
propagate the exception instead

--------------------------------------------------------------------------------
You can use the @contextmanager decorator to turn a generator
function into a function-based context manager.

The generator function must have a yield statement, which
separates the setup code (before yield) from the teardown
code (after yield). The setup code runs when the execution enters
the context, and the teardown code runs when it exits the
context:

```python
from contextlib import contextmanager

@contextmanager
def hello_context_manager():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")
```

The object that the yield statement produces is what
`.__enter__()` would return in a class-based context
manager. This approach saves you from writing a class with
`.__enter__()` and `.__exit__()` methods, which means that you’ll
need to write less boilerplate code.

--------------------------------------------------------------------------------
Due to Python’s Global Interpreter Lock (GIL), threading is
restricted to running Python bytecode a single CPU core at one
time. The `multiprocessing` library will allow you to run code in
parallel on different CPU cores.

--------------------------------------------------------------------------------

The `.join()` method allows one thread to wait for a second
thread to complete. It is done automatically for you when you use
a `ThreadPoolExecutor` as a context manager (a with statement).

--------------------------------------------------------------------------------
A race condition is when two threads interfere with each other
while accessing a shared resource. The resource can be a variable
in memory, a file, or a physical device like a serial port.

--------------------------------------------------------------------------------
Using a `ThreadPoolExecutor` to manage your threads as a context
manager takes care of starting and waiting for each thread in
your pool. It does not, however, pass exceptions from the Thread
pool back to the main program well. It also does not prevent race
conditions.

--------------------------------------------------------------------------------
Python compiles your source code into bytecode to speed up the
startup time of your scripts. The interpreter can skip recurring
steps such as lexing and parsing the code into an abstract syntax
tree and validating its correctness every time you run the same
program.

As long as the underlying source code hasn’t changed, Python can
reuse the bytecode, which is immediately ready for
execution. However, loading the compiled bytecode from
`__pycache__` doesn’t affect the execution speed of your scripts.

--------------------------------------------------------------------------------
```
python -X importtime script.py
```

You can pass the -X importtime option to the python command to
measure and display the time it takes to import each module.

When you run a Python script with this option, Python will
display a table summarizing how long it took to import each
module, including the cumulative time in case a module depends on
other modules.

You can use this option to measure the difference in import time
between a cached and uncached module.

--------------------------------------------------------------------------------
The .pyc extension stands for a Python compiled file or, more
specifically, a compiled Python module. Such a file contains the
bytecode of the corresponding Python module, defined in the
current package, that you imported at runtime. The compiled
bytecode targets a specific Python implementation, version, and
an optional optimization level. All of this information is
encoded in the file name.

For example, a file named arithmetic.pypy310.opt-2.pyc is the
bytecode of an arithmetic.py module compiled by PyPy 3.10 with an
optimization level of two. This optimization removes the assert
statements and discards any docstrings. Conversely,
arithmetic.cpython-312.pyc represents the same module but
compiled for CPython 3.12 without any optimizations.

--------------------------------------------------------------------------------
Python creates the `__pycache__` folders and compiles modules
into .pyc files when you import custom modules or their parent
package for the first time or after modifying their source code.

This is based on the assumption that modules are less likely to
change and that you may import them multiple times during a
single execution. The interpreter won’t create the cache folder
when you run a regular Python script that doesn’t import any
modules or packages.

--------------------------------------------------------------------------------
Python uses two cache invalidation strategies to determine
whether a module needs recompiling: timestamp-based and
hash-based.

The timestamp-based strategy compares the source file’s size and
its last modification to the metadata stored in the corresponding
.pyc file.

The hash-based strategy calculates the digest of the source file
and checks it against a special field in the file’s header.

--------------------------------------------------------------------------------
If you don’t want Python to cache the compiled bytecode, then you
can pass the -B option to the python command when running a
script. This will prevent the `__pycache__` folders from
appearing unless they already exist. Python will continue to
leverage any .pyc files that it can find in existing cache
folders. It just won’t write new files to disk.

For a more permanent and global effect that spans across multiple
Python interpreters, you may consider setting the
`PYTHONDONTWRITEBYTECODE` environment variable in your shell or its
configuration file:

```
export PYTHONDONTWRITEBYTECODE=1
```

It’ll affect any Python interpreter, including one within a
virtual environment that you’ve activated.

Still, you should think carefully whether suppressing bytecode
compilation is the right approach for your use case. The
alternative is to tell Python to create the individual
`__pycache__` folders in a single shared location on your file
system.

--------------------------------------------------------------------------------
You can instruct Python to store the bytecode cache in a specific
directory by using the -X pycache_prefix option when running
Python:

```
$ python -X pycache_prefix=/tmp/pycache calculator.py
```

Alternatively, you can set the `PYTHONPYCACHEPREFIX` environment
variable:

```
export PYTHONPYCACHEPREFIX=/tmp/pycache
```

In this case, Python caches the compiled bytecode in a temporary
folder located at /tmp/pycache on your file system. Python won’t
try to create local __pycache__ folders in your project
anymore. Instead, it’ll mirror the directory structure of your
project under the indicated root folder and store all .pyc files
there.

--------------------------------------------------------------------------------
Python represents bytecode as code objects, which are serialized
in the .pyc files using the marshal module.

--------------------------------------------------------------------------------
While you can import compiled modules from ZIP files or by hand,
this only provides a rudimentary form of code obfuscation. More
tech-savvy users could try to decompile your `.pyc` files back into
high-level Python code using specialized tools.

A more secure way to conceal Python source code is by compiling
it to machine code. You can do this with tools like Cython, or by
rewriting the core parts of your code in a lower-level
programming language like C, C++, or Rust.

--------------------------------------------------------------------------------
The dis module in Python’s standard library allows you to
disassemble the compiled bytecode. This can be useful for
understanding the lower-level workings of your Python code.

Here’s an example of how you might use it:

```python
from pathlib import Path
source_code = Path("arithmetic.py").read_text(encoding="utf-8")
module = compile(source_code, "arithmetic.py", mode="exec")

from dis import dis
dis(module)
```

This will output the human-readable opcode names of the resulting
code object. You can see the opcodes MAKE_FUNCTION and STORE_NAME
which tell you that there’s a function named add() in this
bytecode. When you look closely at the disassembled code object
of that function, you’ll see that it takes two arguments called a
and b, adds them using the binary plus operator (+), and returns
the calculated value.
