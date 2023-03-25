from classes.stack import Node


# class Node:
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next_node = next_node


class LinkedList:
    list_data = []
    """Класс для создания связанного списка"""

    def __init__(self, beginning=None, end=None):
        self.beginning = beginning
        self.end = end

    def insert_beginning(self, data):
        """Метод для добавления данных в начало списка"""
        beginning_node = Node(data)
        if self.beginning is None:
            self.end = beginning_node
        else:
            beginning_node.next_node = self.beginning
        self.beginning = beginning_node

    def insert_at_end(self, data):
        """Метод для добавления данных в конец списка"""
        node_at_end = Node(data)
        if self.beginning is None:
            self.beginning = node_at_end
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

    def to_list(self):
        """Метод для получения списка данных из односвзяного списка"""
        current_node = self.beginning
        while current_node.next_node is not None:
            self.list_data.append(current_node.data)
            current_node = current_node.next_node
        self.list_data.append(current_node.data)
        return self.list_data

    def get_data_by_id(self, user_id):
        """Метод для получения данных о пользователе по его id"""
        current_node = self.beginning
        while current_node:
            if isinstance(current_node.data, dict) and "id" in current_node.data:
                if user_id == current_node.data['id']:
                    return current_node.data

            else:
                print("Данные не являются словарем или в словаре нет id")
            current_node = current_node.next_node
        # current_node = self.beginning
        # try:
        #     while current_node:
        #         if user_id == current_node.data['id']:
        #             return current_node.data
        #
        #         current_node = current_node.next_node
        # except TypeError:
        #     print("Данные не являются словарем или в словаре нет id")

        # current_node = self.beginning
        # while current_node is not None:
        #     try:
        #         if current_node.data.get('id') == user_id:
        #             return current_node.data
        #         current_node = current_node.next_node
        #     except AttributeError:
        #         print("Данные не являются словарем или в словаре нет id")
        #         break
        # return None


# ll = LinkedList()
# ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
# ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
# ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
# ll.insert_beginning({'id': 0, 'username': 'serebro'})
# lst = ll.to_list()
# print(lst)
# for item in lst: print(item)


ll = LinkedList()

ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})

user_data = ll.get_data_by_id(2)
print(user_data)
