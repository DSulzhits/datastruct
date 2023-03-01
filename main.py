from classes.classes import Node, Stack


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
    stack = Stack()
    stack.push('data1')
    data = stack.pop()
    print(stack.top)
    print(data)
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    data = stack.pop()
    print(stack.top.data)
    print(data)
    data = stack.pop()
    print(data)


if __name__ == "__main__":
    main()
