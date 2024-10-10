


.PHONY: build
build: clean
	./build.py
	zip calisthenics.zip index.html pico.min.css


.PHONY: clean
clean:
	rm -f index.html calisthenics.zip


.PHONY: serve
serve:
	python -m http.server

