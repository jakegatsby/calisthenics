

.PHONY: build
build:
	./build.py
	zip calisthenics.zip index.html pico.min.css

.PHONY: serve
serve:
	python -m http.server

