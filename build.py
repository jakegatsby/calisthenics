#!/usr/bin/env python

import markdown
import jinja2


env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"), autoescape=False)
template = env.get_template("index.html.j2")


with open("wod.md") as f:
  wod = markdown.markdown(f.read())


with open("calisthenics.md") as f:
  calisthenics = markdown.markdown(f.read())


with open("mobility.md") as f:
  mobility = markdown.markdown(f.read())


with open("index.html", "w") as f:
  f.write(template.render(wod=wod, calisthenics=calisthenics, mobility=mobility))

