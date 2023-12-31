install:
	poetry install

build:
	poetry build

test-publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

brain-games:
	poetry run brain-games