#!/usr/bin/env python

import markdown
import jinja2


env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"), autoescape=False)
template = env.get_template("index.html.j2")

with open("skills.md") as f:
  skills = markdown.markdown(f.read())

with open("mobility.md") as f:
  mobility = markdown.markdown(f.read())

with open("prehab_rehab.md") as f:
  prehab_rehab = markdown.markdown(f.read())



with open("index.html", "w") as f:
  f.write(template.render(skills=skills, mobility=mobility, prehab_rehab=prehab_rehab))

