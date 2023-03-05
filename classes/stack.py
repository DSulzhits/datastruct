class Node:
    """Добавлен класс для работы с односвязным списком принимающий данные и ссылку на следующий узел с данными
    1й узел None, 2й на 1й и т.д."""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    """Добавлен класс для работы со стеком"""

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Метод для последовательного добавления данных в стэк"""
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Метод для последовательного удаления данных из стэка"""
        remove_last = self.top
        self.top = self.top.next_node
        return remove_last.data


