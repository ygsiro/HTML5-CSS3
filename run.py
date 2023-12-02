import json

with open("list.json") as a_f:
    elements = json.load(a_f)
    for key, value in elements.items():
        print(f'<li><a href="{key}.html">{key}</a></li>')
