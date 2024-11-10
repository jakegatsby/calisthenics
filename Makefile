.PHONY: build
build: clean
	./build.py
	zip site.zip index.html pico.min.css


.PHONY: clean
clean:
	rm -f index.html site.zip


.PHONY: serve
serve:
	python -m http.server


.PHONY: publish
publish:
	firefox https://dash.cloudflare.com/a7700637397b3281f1891768d30c8768/pages/view/gymnastics-calisthenics

.PHONY: view
view:
	firefox https://gymnastics-calisthenics.pages.dev/
