#!/usr/bin/env python

import markdown
import jinja2

with open("README.md") as f:
  content = markdown.markdown(f.read())


env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"), autoescape=False)
template = env.get_template("index.html.j2")

with open("index.html", "w") as f:
  f.write(template.render(content=content))

