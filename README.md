# About

`andrewtools` is an assortment of handy Python tools made by someone named Andrew.

# Quick Start

## Support Python Versions

Python 3.8+

## Mac / Linux
```
pip install andrewtools
```

## Windows
```
py -m pip install andrewtools
```

## Examples
----

## Progress Bar

Print a progress bar for a loop in-place to the standard output

```
import time
from andrewtools import print_progress_bar

iterations = 10
for i in range(iterations):
    print_progress_bar(i, iterations, width=10, prefix="Progress")
    time.sleep(0.5)

# Printed to standard out:
Progress | ***------- | 30%
```