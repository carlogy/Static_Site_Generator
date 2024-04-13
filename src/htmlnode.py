
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props is None:
            return ""
        if self.props is not None:
            props_list = []
            for key, value in self.props.items():
                props_list.append(f" {key}=\"{value}\"")
            return "".join(props_list)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, otherNode) -> bool:
        return (
            self.tag == otherNode.tag
            and self.value == otherNode.value
            and self.children == otherNode.children
            and self.props == otherNode.props
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props) -> None:
        super().__init__(tag, value, props)
        self.tag = tag
        self.value = value
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __eq__(self, otherNode) -> bool:
        return (
            self.tag == otherNode.tag
            and self.value == otherNode.value
            and self.props == otherNode.props
        )

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props) -> None:
        super().__init__(tag, children, props)
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag == None:
            raise ValueError("Improper html, html tag is not present")
        if self.children is None:
            raise ValueError("Parent has no children")

        html_children = []
        for i in range(len(self.children)):
            if self.children[i].tag is None and self.children[i].props is None:
                html_children.append(f"{self.children[i].value}")
            html_children.append(f"<{self.children[i].tag}{self.children[i].props_to_html()}>{self.children[i].value}</{self.children[i].tag}>")
        complete_html = f"<{self.tag}{self.props_to_html()}>{"".join(html_children)}</{self.tag}>"
        return complete_html

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
