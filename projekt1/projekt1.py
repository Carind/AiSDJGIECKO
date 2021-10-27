from typing import Any


class Node:
    value: Any
    next: 'Node'

    def __init__(self, data=None, next=None):
        self.value: Any = data
        self.next: Node = next


class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        out: str = ""
        current = self.head
        while (current):
            out += str(current.value)
            out += ' -> '
            current = current.next
        return out[:-4]

    def __print__(self):
        out: str = ""
        current = self.head
        while (current):
            out += str(current.value)
            out += ' -> '
            current = current.next
        print(out[:-4])

    def push(self, val: Any):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def append(self, val: Any):
        newNode = Node(val)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            self.tail = newNode
    def append2(self, val: Any):
        newNode = Node(val)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.tail
            self.tail = newNode

    def node(self, at: int) -> Any:
        id: int = 0
        current_node = self.head
        while at > id and current_node is not None:
            current_node = current_node.next
            id += 1
        return current_node.value

    def insert(self, val: int, after: Node) -> None:
        newNode = Node(val)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
                if current.value == after:
                    newNode.next = current.next
                    current.next = newNode

        else:
            self.head = newNode

    def pop(self) -> Any:
        if self.head is None:
            return -1
        else:
            out: Any = self.head.value
            self.head = self.head.next
            return out

    def remove_last(self) -> Any:
        if (self.head):
            current = self.head
            while (current.next.next):
                current = current.next
            out: Any = current.next.value
            current.next = None
            return out
        else:
            return -1

    def remove(self, after: node) -> Any:
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
                if current.value == after:
                    if current.next.next == self.head:
                        current.next = self.head
                    if current.next.next == self.tail:
                        current.next = self.tail
                    current.next = current.next.next


    def __len__(self) -> int:
        out: int = 0
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            out += 1
        return out

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)

assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
assert last_element == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def __len__(self) -> int:
        return len(self._storage)

    def push(self, element: Any) -> None:
        self._storage.push(element)

    def pop(self) -> Any:
        return self._storage.pop()

    def print(self):
        stack2 = self
        while len(stack2)>0:
            print(stack2.pop())

    def __str__(self) -> str:
        out: str = ""
        if (self._storage.head):
            current = self._storage.head
            while (current):
                out += str(current.value)
                out += '\n'
                current = current.next
        return out[:-1]


stack = Stack()

assert len(stack) == 0

stack.push(3)
stack.push(10)
stack.push(1)

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1
assert len(stack) == 2
class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def __str__(self) -> str:
        out: str = ""
        if (self._storage.head):
            current = self._storage.head
            while (current):
                out += str(current.value)
                out += ', '
                current = current.next
        return out[:-2]

    def __len__(self) -> int:
        return len(self._storage)

    def peek(self) -> Any:
        if (self._storage.head):
            return self._storage.head.value
        else:
            return -1

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

queue = Queue()
assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
