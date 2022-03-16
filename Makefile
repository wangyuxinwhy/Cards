# Makefile

.PHONY: help
help:
	@echo "Commands:"
	@echo "style  : format files"
	@echo "test    : test program"

.PHONY: style
style:
	flake8 .
	black .
	isort --profile black .

.PHONY: clean
clean:
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E "(\.hypothesis)" | xargs rm -rf
	rm -rf dist
	rm -rf simpletrainer.egg-info
	find . | grep experiments | xargs rm -rf
	rm -f .coverage

.PHONY: test
test:
	pytest
