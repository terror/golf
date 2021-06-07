all: fmt test

fmt:
  yapf --in-place --recursive --style="{indent_width: 2}" **/*.py

test:
  pytest .
