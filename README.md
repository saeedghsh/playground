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

# License
```
Copyright (C) Saeed Gholami Shahbandi
```

NOTE: Portions of this code/project were developed with the assistance of ChatGPT, a product of OpenAI.  
Distributed with a GNU GENERAL PUBLIC LICENSE; see [LICENSE](https://github.com/saeedghsh/playground/blob/master/LICENSE).

