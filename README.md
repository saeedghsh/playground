# Playground

[![GPLv3 License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/saeedghsh/playground/blob/master/LICENSE)  
[![black](https://github.com/saeedghsh/playground/actions/workflows/formatting.yml/badge.svg?branch=master)](https://github.com/saeedghsh/playground/actions/workflows/formatting.yml)
[![pylint](https://github.com/saeedghsh/playground/actions/workflows/pylint.yml/badge.svg?branch=master)](https://github.com/saeedghsh/playground/actions/workflows/pylint.yml)
[![pytest](https://github.com/saeedghsh/playground/actions/workflows/pytest.yml/badge.svg?branch=master)](https://github.com/saeedghsh/playground/actions/workflows/pytest.yml)
[![pytest-cov](https://github.com/saeedghsh/playground/actions/workflows/pytest-cov.yml/badge.svg?branch=master)](https://github.com/saeedghsh/playground/actions/workflows/pytest-cov.yml)
[![mypy](https://github.com/saeedghsh/playground/actions/workflows/type-check.yml/badge.svg?branch=master)](https://github.com/saeedghsh/playground/actions/workflows/type-check.yml)


* Lorenz system ([read more](https://github.com/saeedghsh/playground/blob/master/docs/lorenz_system.md)).
* Collatz conjecture ([read more](https://github.com/saeedghsh/playground/blob/master/docs/collatz_conjecture.md)).
* Stochastic processes ([read more](https://github.com/saeedghsh/playground/blob/master/docs/stochastic_processes.md)).
* Coordinate transformation ([read more](https://github.com/saeedghsh/playground/blob/master/docs/transformation.md)).
* Chaotic systems  ([read more](https://github.com/saeedghsh/playground/blob/master/docs/chaotic_system.md)).

Next in line:
* [Ackermann steering geometry](https://en.m.wikipedia.org/wiki/Ackermann_steering_geometry)
* constraint programming:
  * https://en.wikipedia.org/wiki/Constraint_programming
  * https://mareknarozniak.com/2020/06/22/constraint-programming/

## Dependencies
```bash
apt install python3-tk
pip install -r requirements.txt
```

## Examples
```bash
python3 -m entry_points.collatz_entry -p graph
python3 -m entry_points.lorenz_entry
python3 -m entry_points.stochastic_processes_entry
python3 -m entry_points.transformation_entry
python3 -m entry_points.chaos_entry logistic-map
```

## Code quality checks
```bash
$ black . --check
$ isort . --check-only
$ mypy . --explicit-package-bases
$ pylint $(git ls-files '*.py')
$ xvfb-run --auto-servernum pytest
$ xvfb-run --auto-servernum pytest --cov=.
$ xvfb-run --auto-servernum pytest --cov=. --cov-report html; firefox htmlcov/index.html
```

## Pyreverse : UML Diagrams for Python
```bash
$ pip install pylint # pyreverse is now part of pylint
$ cd ~/code/ChaoticSystems
$ pyreverse -o svg -p chaos chaos/*.py
$ pyreverse -o svg -p chaoticSystems main.py
$ pyreverse -o svg -p tests/*.py
# -a N, -A    depth of research for ancestors
# -s N, -S    depth of research for associated classes
# -A, -S      all ancestors, resp. all associated
# -m[yn]      add or remove the module name
# -f MOD      filter the attributes : PUB_ONLY/SPECIAL/OTHER/ALL
# -k          show only the classes (no attributes and methods)
# -b          show 'builtin' objects
```

## Laundry list
* [ ] unittest is virtually non-existent
* [ ] update the commands under Pyreverse section
* [ ] There are too many warning suppression, remove and fix


# License
```
Copyright (C) Saeed Gholami Shahbandi
```

NOTE: Portions of this code/project were developed with the assistance of ChatGPT, a product of OpenAI.  
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/playground/blob/master/LICENSE).

