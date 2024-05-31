# Playground


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

## To play with
* [Ackermann steering geometry](https://en.m.wikipedia.org/wiki/Ackermann_steering_geometry)
* constraint programming:
  * https://en.wikipedia.org/wiki/Constraint_programming
  * https://mareknarozniak.com/2020/06/22/constraint-programming/
* 

## Laundry list
* [ ] unittest is virtually non-existent
* [ ] each subdirectory should have a proper `README.md`
* [ ] list all sub-projects in this repo here in this `README.md`

# License
```
Copyright (C) Saeed Gholami Shahbandi
```

NOTE: Portions of this code/project were developed with the assistance of ChatGPT, a product of OpenAI.  
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/playground/blob/master/LICENSE).

