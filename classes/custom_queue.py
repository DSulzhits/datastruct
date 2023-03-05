from classes.stack import Node, Stack


class Queue:
    """Создан класс для работы с очередью"""

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Написан метод для добавления элементов в очередь"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node
