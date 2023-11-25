from src.entity.base import Base


class Node(Base):
    def __init__(self, data):
        self.data = data
        self.childrens = []

    def add_child(self, children):
        self.childrens.append(children)

        return children
