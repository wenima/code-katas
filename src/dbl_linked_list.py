"""Create a Double Linked List Data Structure. A doubly linked list is a
linked data structure that consists of a set of sequentially linked records
called nodes. Each node contains two fields, called links, that are references
to the previous and to the next node in the sequence of nodes. The beginning and
ending nodes' previous and next links, respectively, point to some kind of
terminator, typically a sentinel node or null, to facilitate traversal of the
list.

Taken from https://en.wikipedia.org/wiki/Doubly_linked_list"""


class DblNode(object):

    """Create Node objects for use in a Linked List data structure.

    Attributes:
        value:      A value or data stored in the Node.
        nxt:        Pointer to the next Node.
        prev:       A pointer to a previus Node.
    """

    def __init__(self, value=None, nxt=None, prev=None):
        """Initialize a Node type object."""
        self.value = value
        self.nxt = nxt
        self.prev = prev


class DblLinkedList(object):

    """Double Linked List (DLL) style Data Structure.

    If initialized with an iterable, will create nodes for each item in
    the iterable.

    Attributes:
        head:       Node on one end of DLL, last item added if
                    initialized with iterable.
        tail:       Node on other end of DLL, first item added if
                    intailized with iterable.
        _size:      The length of the DLL or number of Nodes stored
                    in the list.

    Methods:
        push(value):    Given a value, add a new Node object to the DLL.

        append(value):  Given a value, adds it at the end of the line.

        pop():          Pop the head Node off the list, return the value.

        shift():        will remove the last value from the line and return it.

        remove(val):    Given a Node, remove that Node from the Linked List.
                        Else, raise a ValueError.
    """

    def __init__(self, maybe_an_iterable=None):
        """Intialize a Double Linked List Object."""
        self.head = None
        self.tail = None
        self._size = 0
        if maybe_an_iterable:
            for value in maybe_an_iterable:
                self.push(value)

    def push(self, value):
        """Add a node at the beginning of list and reassign head."""
        new = DblNode(value)
        if self._size > 0:
            old = self.head
            self.head = new
            new.nxt = old
            old.prev = new
        else:
            self.head = new
            self.tail = self.head
        self._size += 1


    def _iterate_from(self, list_item):
        """Return a generator."""
        while list_item is not None:
            yield list_item
            list_item = list_item.nxt

    def generate_list_of_nodes(self):
        """Return a list of nodes."""
        nodes = [node for node in self._iterate_from(self.head)]
        return nodes
