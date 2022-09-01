"""
Implementation of a Singly Linked List based on Nodes
"""


class Node:
    """
    A base item of LinkedList, has data and a link to next Node in link stored in attributes
    """
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        """
        Changes str representation of Node to its data value
        :return: Node data value
        """
        return self.data


class LinkedList:
    """
    A class that utilizes Nodes to form a linked structure
    """
    def __init__(self, nodes: list = None):
        """
        This method allows to create an empty LinkedList or a LinkedList with data from a list
        :param nodes:
        """
        self.head = None
        if nodes is not None:
            current_node = Node(data=nodes.pop(0))
            self.head = current_node
            for elem in nodes:
                current_node.next = Node(data=elem)
                current_node = current_node.next

    def __str__(self):
        """
        Changes str representation of a LinkedList to a visual display e.g. "a -> b -> c -> None"
        :return: visual display of a LinkedList
        """
        current_node = self.head
        nodes = []
        while current_node is not None:
            nodes.append(current_node.data)
            current_node = current_node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """
        allows iteration through all length of LinkedList
        :return: node data
        """
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def push(self, new_node_data):
        """
        Inserts a new node at the beginning of the LinkedList
        :param new_node_data: new node data
        :return: None
        """
        new_node = Node(new_node_data)
        new_node.next = self.head
        self.head = new_node

    def append(self, new_node_data):
        """
        Inserts a new node at the end of the LinkedList
        :param new_node_data: new node data
        :return: None
        """
        new_node = Node(new_node_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_after(self, target_node_data, new_node_data):
        """
        The method adds a node after first found existing node with a specific data value
        :param target_node_data: data value to insert new node after
        :param new_node_data: new node data
        :return:
        """
        if self.head is None:
            raise Exception("LinkedList is empty")

        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_node_data)
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")

    def insert_before(self, target_node_data, new_node_data):
        """
        The method adds a node before an existing node with a specific data value
        :param target_node_data: data value to insert new node before
        :param new_node_data: new node data
        :return:
        """
        if self.head is None:
            raise Exception("LinkedList is empty")

        if self.head.data == target_node_data:
            return self.push(new_node_data)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                new_node = Node(new_node_data)
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def delete_node(self, target_node_data):
        """
        The method deletes the first node with a specific data value
        :param target_node_data: data value to delete
        :return:
        """
        if self.head is None:
            raise Exception("LinkedList is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def pop(self):
        """
        The method deletes the last node and returns its data
        :return: data of deleted node
        """
        if self.head is None:
            raise Exception("LinkedList is empty")

        if self.head.next is None:
            popped_data = self.head.data
            self.head = None
            return popped_data
        else:
            pre_last = self.head
            last = self.head.next
            while last.next:
                pre_last = last
                last = last.next
            popped_data = last.data
            pre_last.next = None
            return popped_data

    def left_pop(self):
        """
        The method deletes the head node and returns its data
        :return: data of deleted node
        """
        if self.head is None:
            raise Exception("LinkedList is empty")

        popped_data = self.head.data
        self.head = self.head.next
        return popped_data


if __name__ == "__main__":
    print('Testing creation of LinkedList')
    l_list = LinkedList(["a", "b", "c", "d", "e"])
    print(l_list)

    print('Testing LinkedList.push()')
    l_list.push("b")
    print(l_list)

    print('Testing LinkedList.insert_after()')
    l_list.insert_after('a', 'f')
    print(l_list)

    print('Testing LinkedList.insert_before()')
    l_list.insert_before('a', 'y')
    print(l_list)

    print('Testing LinkedList.delete_node()')
    l_list.delete_node('y')
    print(l_list)

    print('Testing LinkedList.pop()')
    popped = l_list.pop()
    print(popped)
    print(l_list)

    print('Testing LinkedList.append()')
    l_list.append(popped)
    print(l_list)

    print('Testing LinkedList.left_pop()')
    popped = l_list.left_pop()
    print(popped)
    print(l_list)

    print('Testing LinkedList iteration')
    for item in l_list:
        print(item)
