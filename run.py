import json


def output(key: str, value: dict):
    with open(f"docs/{key}.html", mode="w", encoding="utf-8") as a_f:
        c_list = []
        for category in value["category"]:
            c_list.append(category.split("/")[0])
        category_list = " ".join(c_list)
        html = f"""<!doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{key}</title>
    <link rel="stylesheet" href="css/style.css">
    <script src="js/script.js" defer></script>
  </head>
  <body>
    <article id="{key}">
    <header class="{category_list}">
      <h1>{key}</h1>
      <ul class="category">
        <li class="meta"></li>
        <li class="flow"></li>
        <li class="section"></li>
        <li class="heading"></li>
        <li class="phrasing"></li>
        <li class="embedded"></li>
        <li class="interactive"></li>
      </ul>
    </header>
    <main>
      <p class="description">{value["description"]}</p>
    </main>
    <footer></footer>
    </article>
  </body>
</html>
"""
        a_f.write(html)


with open("list.json") as a_f:
    elements = json.load(a_f)
    for key, value in elements.items():
        output(key, value)
