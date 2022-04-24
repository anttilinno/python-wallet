# VERSION 1.0

Just find out, how to make web requests and read yaml. Building
horrible code is easy :smile:

# VERSION 2.0

Hello objects. Create two simple classes and run with it. There
was a problem, I could not make structure.

# VERSION 3.0

Started reading **"Learning Python, 5th Edition"** , but this version was created prior reading the chapter about OOP. I read an article in [realpython](https://realpython.com/python3-object-oriented-programming/).

Started to use [pdm](https://pdm.fming.dev/). Structured code to main module *wallet* and submodule *coin*. Wrote tests. Created [Makefile](https://earthly.dev/blog/python-makefile/), so I don't have to remember different pdm commands.

Code structure was taken from [realpython](https://realpython.com/python-application-layouts/) again.

<h2 style="text-align: center;">Problems</h2>

* Testing exception imports is hard (how do you test exception?)

    ```
    try:
        from yaml import CLoader as Loader, CDumper as Dumper
    except ImportError:
        from yaml import Loader, Dumper
    ```

    Hints could be gleaned from https://www.scivision.dev/pytest-skip-importerror/

* How to test main function?

    https://www.pylenin.com/blogs/if-name-equal-to-main/

* How to compare objects in tests?
    
    https://igeorgiev.eu/python/tdd/python-unittest-assert-custom-objects-are-equal/
