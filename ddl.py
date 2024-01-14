from typing import Union


class Node:
    def __init__(self, key, prev=None, child=None):
        self.key: float = key
        self.prev: Union[Node, None] = prev
        self.child: Union[Node, None] = child


class DoubleLinkedList:
    def __init__(self):
        self.head: Union[Node, None] = None

    def list_insert(self, value):
        if self.head is None:
            self.head = Node(key=value)
        else:
            self.head = Node(key=value, child=self.head)
            self.head.child.prev = self.head


if __name__ == '__main__':
    ...