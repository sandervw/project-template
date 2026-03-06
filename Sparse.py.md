# The Laws of Sparse Python

## The Primary Laws

1. All Sparse Python Laws must adhere to the Laws defined in `Sparse.md`. `No Exceptions.`
2. All Python specific Sparse Laws must be specified within this file. `No Exceptions.`

## Python Specific Laws

3. All Python files must include `from __future__ import annotations` as the first import. `No Exceptions.`
4. All function parameters and return values must have explicit type annotations. `No Exceptions.`
5. All mutable default arguments must be `None` with the actual default assigned inside the function body. `No Exceptions.`
6. All imports must be grouped in the following order (separated by a blank line between each group): standard library, third-party, local. `No Exceptions.`
7. All wildcard imports (`from x import *`) are forbidden. `No Exceptions.`
8. All data-only objects must use `dataclasses` or `NamedTuple`, not plain `__init__` methods. `No Exceptions.`
9. All string formatting must use f-strings, not `%` formatting or `.format()`. `No Exceptions.`
10. All modules must be no longer than 300 lines. `No Exceptions.`
11. All resource acquisition (files, locks, connections, transactions) must use context managers (`with`). `No Exceptions.`
12. All exceptions caught must specify an explicit exception type, never bare `except:` or `except Exception:`. `No Exceptions.`

`No Exceptions.`
