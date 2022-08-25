def solution(node):
    n = node
    m = node.next
    n.prev = m
    n.next = None
    while m is not None:
        m.prev = m.next
        m.next = n
        n = m
        m = m.prev
    node = n
    return node