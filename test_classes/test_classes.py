import unittest
from classes.classes import Node, Stack


class TestNode(unittest.TestCase):
    def test_Node(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertEqual(node.next_node, None)
        node1 = Node(5, node)
        self.assertEqual(node1.data, 5)
        self.assertEqual(node1.next_node, node)


class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
        stack.push('data')
        self.assertEqual(stack.top.data, 'data')

    def test_pop(self):
        stack = Stack()
        stack.push('data1')
        data = stack.pop()
        self.assertEqual(stack.top, None)
        self.assertEqual(data, 'data1')


