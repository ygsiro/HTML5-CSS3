class Node:
    def __init__(
        self, name: str, id: str | None = None, class_: str | None = None, **kwargs
    ):
        """
        name: タグ名。半角英字のみ推奨、空白禁止、名前空間は考慮しない
        id: ID. 半角英字のみ推奨。
        class_: クラス。引数で指定する場合classが使用できないため_付
        kwargs: その他属性
        """
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
        """
        key: 属性名
        value: 属性の値
        """
        self.__attr[key] = value

    def __getitem__(self, key: str) -> str:
        """
        key: 属性名
        return: 属性の値
        """
        return self.__attr.get(key, "")

    def html_string(self, lank: int = 0) -> str:
        """
        HTML形式で表現
        """
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
        """
        子要素の追加
        Nodeを継承したクラスしか追加できません
        """
        if issubclass(type(node), Node):
            node.__root = self.__root
            node.__parent = self
            self.__child.append(node)

    def getId(self) -> str:
        """
        IDの取得
        """
        return self.__attr.get("id", "")

    def getClass(self) -> list[str]:
        """
        CLASSリストの取得
        """
        return self.__attr.get("class", "").split()


class TextNode(Node):
    def __init__(self, text: str):
        """
        text: テキスト
        """
        super().__init__("text")
        self.text = text
        self.__root = self
        self.__parent = None

    def __setitem__(self, key: str, value: str):
        """
        属性はなし
        """
        pass

    def __getitem__(self, key: str) -> str:
        """
        属性はなし
        """
        return ""

    def html_string(self, lank: int = 0) -> str:
        """
        文字を返す
        """
        return lank * "  " + f"{self.text}\n"

    def getId(self) -> str:
        """
        IDは無し
        """
        return ""

    def getClass(self) -> list[str]:
        """
        CLASSは無し
        """
        return []

    def append(self, node):
        """
        子要素は追加できない
        """
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
