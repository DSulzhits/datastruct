from classes.stack import Node


# class Node:
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node


class LinkedList:
    """Класс для создания связанного списка"""
    def __init__(self, beginning=None, end=None):
        self.beginning = beginning
        self.end = end

    def insert_beginning(self, data):
        """Метод для добавления данных в начало списка"""
        beginning_node = Node(data)
        if self.beginning is None:
            self.beginning = beginning_node
            self.end = beginning_node
        else:
            beginning_node.next_node = self.beginning
            self.beginning = beginning_node

    def insert_at_end(self, data):
        """Метод для добавления данных в конец списка"""
        node_at_end = Node(data)
        if self.beginning is None:
            self.beginning = node_at_end
            self.end = node_at_end
        else:
            self.end.next_node = node_at_end
            self.end = node_at_end

    def print_ll(self):
        ll_string = ''
        node = self.beginning
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)


# ll = LinkedList()
# ll.insert_beginning({'id': 1})
# ll.insert_at_end({'id': 2})
# ll.insert_at_end({'id': 3})
# ll.insert_beginning({'id': 0})
# ll.print_ll()
