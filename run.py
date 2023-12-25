import json

with open("list.json") as a_f:
    elements: dict = json.load(a_f)
    test = list(elements.keys())
    test.sort()
    for i in test:
        print(i)
