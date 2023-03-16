import unittest
from classes.stack import Node, Stack
from classes.custom_queue import Queue


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


class TestQueue(unittest.TestCase):

    def test_init(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)
        queue1 = Queue('data_head', 'data_tail')
        self.assertEqual(queue1.head, 'data_head')
        self.assertEqual(queue1.tail, 'data_tail')

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        self.assertEqual(queue.head.data, 'data1')
        self.assertEqual(queue.tail.data, 'data1')
        queue.enqueue('data2')
        self.assertEqual(queue.head.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data2')
        self.assertEqual(queue.tail.next_node, None)

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        self.assertEqual(queue.dequeue(), 'data1')
        self.assertEqual(queue.dequeue(), 'data2')
        self.assertEqual(queue.dequeue(), None)





