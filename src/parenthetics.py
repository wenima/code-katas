"""Program to parse an input string containing parantheses.

Following statements are true:

A string of parantheses is broken if it a close parantheses ')' is encountered
before it's opened and should return -1.

A string of parantheses is deemed open if one or more open parantheses ('(')
are not matched by a closing parantheses and should return 1.

Finally, a string of parantheses is considered balanced if all parantheses are
matched."""

from dbl_linked_list import DblLinkedList


def parse_parentheses(s):
    ps = DblLinkedList(s[::-1])
    nodes = ps.generate_list_of_nodes()
    if nodes[0].value == ')':
        return -1
    elif nodes[-1].value == '(':
        return 1
    return check_match(nodes)


def check_match(nodes):
    idx_open = [i for i, x in enumerate(nodes) if x.value == '(']
    idx_closed = [i for i, x in enumerate(nodes) if x.value == ')']
    if len(idx_open) > len(idx_closed):
        return 1
    for i in (range(len(idx_open))):
        if idx_open[i] > idx_closed[i]:
            return -1
    return 0
