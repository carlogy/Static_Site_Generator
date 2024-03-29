class HTMLNode:
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if type(self.props) == dict:
            props_html = ''.join([f' {key}="{value}"' for key, value in self.props.items()])
            return props_html
        else:
            raise ValueError("Props are not python dictionary")

    def __repr__(self) -> str:
        return f"{self}({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError("Empty HTML tag: No Value Provided.")
        if self.tag == None or self.tag == "":
            return f'{self.value}'
        if self.props != dict:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("No html tags don't exist.")

        if self.children is None:
            raise ValueError("No children nodes exists.")

        html_list = []
        html_list.append(f"<{self.tag}>")

        for child in self.children:
           child_html = child.to_html()

           html_list.append(child_html)

        html_list.append(f"</{self.tag}>")
        return ''.join(html_list)
