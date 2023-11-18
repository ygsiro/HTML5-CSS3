class Node:
    def __init__(
        self, name: str, id: str | None = None, class_: str | None = None, **kwargs
    ):
        self.__name = name
        self.__attr = kwargs
        if id:
            self.__attr[id] = id
        if class_:
            self.__attr["class"] = class_
        self.__child = []
        self.__root = self
        self.__parent = None

    def __setitem__(self, key: str, value: str):
        self.__attr[key] = value

    def __getitem__(self, key: str) -> str:
        return self.__attr.get(key, "")

    def html_string(self, lank: int = 0) -> str:
        result = lank * "  " + f"<{self.__name}"
        for k, v in self.__attr.items():
            result += f' {k}="{v}"'
        if self.__child:
            result += ">\n"
            for i in self.__child:
                result += i.html_string(lank + 1)
            result += lank * "  " + f"</{self.__name}>\n"
        else:
            result += "/>\n"
        return result

    def append(self, node):
        if issubclass(type(node), Node):
            node.__root = self.__root
            node.__parent = self
            self.__child.append(node)

    def getId(self) -> str:
        return self.__attr.get("id", "")

    def getClass(self) -> list[str]:
        return self.__attr.get("class", "").split()


class TextNode(Node):
    def __init__(self, text: str):
        super().__init__("text")
        self.text = text
        self.__root = self
        self.__parent = None

    def __setitem__(self, key: str, value: str):
        pass

    def __getitem__(self, key: str) -> str:
        return ""

    def html_string(self, lank: int = 0) -> str:
        return lank * "  " + f"{self.text}\n"

    def getId(self) -> str:
        return ""

    def getClass(self) -> list[str]:
        return []

    def append(self, node):
        pass


a = Node("html", lang="ja")
b = Node("head")
c = Node("meta", charset="utf-8")
d = Node("title")
e = Node("body")
d.append(TextNode("Sample"))
a.append(b)
b.append(c)
b.append(d)
a.append(e)
print(a.html_string())
