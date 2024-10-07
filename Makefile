

.PHONY: build
build:
	./build.py


.PHONY: serve
serve:
	python -m http.server
