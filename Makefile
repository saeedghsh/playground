SHELL := /bin/bash


all: \
	clean \
	formatter \
	lint-flake8 \
	test \
	verify-clean-git-stage

.PHONY: tidy-up
tidy-up: \
	clean \
	formatter \
	lint-flake8 

.PHONY: clean
clean: \
	clean-pyc \
	clean-pytest-cach \
	clean-build

.PHONY: formatter
formatter: \
	formatter-isort \
	formatter-black

.PHONY: clean-pyc
clean-pyc:
	@echo "***** rm *.pyc *.pyo *~"
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~'    -exec rm -f {} +

.PHONY: clean-pytest-cach
clean-pytest-cach:
	@echo "***** rm .pytest_cache"
	@rm -rf .pytest_cache

.PHONY: clean-build
clean-build:
	@echo -e "***** rm -rf build/ dist/ *.egg-info"
	@rm -rf build/
	@rm -rf dist/
	@rm -rf *.egg-info

.PHONY: formatter-isort
formatter-isort:
	@echo -e "***** formatter with isort"
	@isort --recursive .

.PHONY: formatter-black
formatter-black:
	@echo -e "***** formatter with black"
	@black .

.PHONY: lint-flake8
lint-flake8:
	@echo -e "***** lint with flake8"
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

.PHONY: test
test:
	@echo -e "***** Running test"
	@pytest

.PHONY: run
run:
	@echo "***** running main.py"
	@python main.py

.PHONY: verify-clean-git-stage
verify-clean-git-stage:
	@echo -e "***** verify cleaniness of git staging area"
	@if [ -n "$$(git status --porcelain)" ]; then git status --porcelain; exit 1; fi
