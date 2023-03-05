from classes.stack import Node, Stack
from classes.custom_queue import Queue


def main():
    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # print(n2.next_node)
    # stack = Stack()
    # stack.push('data1')
    # stack.push('data2')
    # stack.push('data3')
    # print(stack.top.data)
    # print(stack.top.next_node.data)
    # print(stack.top.next_node.next_node.data)
    # print(stack.top.next_node.next_node.next_node)
    # stack = Stack()
    # stack.push('data1')
    # data = stack.pop()
    # print(stack.top)
    # print(data)
    # stack = Stack()
    # stack.push('data1')
    # stack.push('data2')
    # data = stack.pop()
    # print(stack.top.data)
    # print(data)
    # data = stack.pop()
    # print(data)
    queue = Queue()
    queue.enqueue('data1')
    queue.enqueue('data2')
    queue.enqueue('data3')

    print(queue.head.data)
    print(queue.head.next_node.data)
    print(queue.tail.data)
    print(queue.tail.next_node)
    print(queue.tail.next_node.data)





if __name__ == "__main__":
    main()
