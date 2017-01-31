"""Program to parse an input string containing parantheses.

Following statements are true:

A string of parantheses is broken if it a close parantheses ')' is encountered
before it's opened and should return -1.

A string of parantheses is deemed open if one or more open parantheses ('(')
are not matched by a closing parantheses and should return 1.

Finally, a string of parantheses is considered balanced if all parantheses are
matched."""

from queue import Queue


def parse_parentheses(s):
    q = Queue(s)
    status = 0
    while len(q) > 0:
        if q.peek() == ')':
            if status == 0:
                return -1
            elif status > 0:
                q.dequeue()
                status -= 1
                continue
        else:
            if status == 0:
                q.dequeue()
                status += 1
            else:
                q.dequeue()
                status += 1
    return 1 if status >= 1 else status
