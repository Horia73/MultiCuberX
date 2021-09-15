
init:
	python3.6 -m venv venv
	@./venv/bin/python3 -m pip install -e .

install:
	python3 setup.py install

clean:
	sudo rm -rf build dist venv
	sudo rm -rf rubikscolorresolver.egg-info rubikscolorresolver/*.pyc rubikscolorresolver/__pycache__

test:
	python3 ./tests/test-unittest.py
	micropython ./tests/test-unittest.py
	python3 ./tests/test-cubes.py
	micropython ./tests/test-cubes.py

checks: black-check lint-check   ## Run all checks (black, lint)

black-check:  ## Check code formatter.
	black --check rubikscolorresolver/ utils/ usr/

black-format:
	black rubikscolorresolver/ utils/ usr/

lint-check:  ## Check linter.
	flake8 --config .flake8 --statistics rubikscolorresolver/ utils/ usr/
