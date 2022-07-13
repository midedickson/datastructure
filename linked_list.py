from requests import head


class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f"Node >> {self.data}"


class LinkedList:
    """
    Singly Linked List
    """
    head = None

    def __init__(self) -> None:
        self.head = None

    def search(self, key):
        """
        Returns the Node or None of they key in its first occurence
        0(n) is the time complexity
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def remove(self, key):
        """
        Remove node that match first occcurence of "key"
        runs in O(n) linear time
        """

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key and current is not self.head:
                found = True
                previous.next_node = current.next_node
            else:
                previous, current = current, current.next_node
        return current

    def remove_at_index(self, index: int) -> None:
        """
        This function removes the node at given index
        Removal Operation runs in constant time O(1)

        Searching for the index runs in linear time O(n)
        """
        current = self.head
        if index == 0:
            current = current.next_node
        else:
            position = 0
            prev_node = current
            while position != index:
                prev_node, current = current, current.next_node
                position += 1

            prev_node.next_node = current.next_node

    def insert(self, data, index):
        """
        Inserts a new node at index position
        Insertion takes constant time O(1)
        but finding the node at insertion position takes O(n)
        Therefore, overall time is O(n)
        """
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)
            position = index
            current = self.head
            while position > 1:
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            new.next_node = next_node
            prev_node.next_node = new

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns number of node, takes linear time 0(n)
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new node with data at the head of the list
        A constant time opearation O(1)
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def reverse(self):
        """
        Reverses the linked list
        """
        current = self.head
        previous = None
        while current:
            next_node = current.next_node
            current.next_node = previous
            previous = current
            current = next_node
        self.head = previous