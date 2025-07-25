VENV := venv
PYTHON := $(VENV)/bin/python
HOST = $(shell ifconfig | grep "inet " | tail -1 | cut -d\  -f2)
TAG = v$(shell grep -E '__version__ = ".*"' team/__init__.py | cut -d\" -f2)

RM := rm -rf

.PHONY: venv clean-build clean-api clean api build

venv:
	$(RM) $(VENV)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install -U --no-cache-dir pip wheel
	$(PYTHON) -m pip install --no-cache-dir setuptools==68.2.2
	$(PYTHON) -m pip install --no-cache-dir -r requirements.txt
	@echo "Created venv with $$($(PYTHON) --version)"

clean-build:
	$(RM) *.egg-info build dist

clean:
	make clean-build
	make clean-api

build:
	make clean
	$(PYTHON) -m pip install --no-cache-dir setuptools==68.2.2
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel
