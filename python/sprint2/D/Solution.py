def solution(node, elem):
    count = 0
    while elem != count:
        if node is None:
            return -1
        if elem == node.value:
            return count
        node = node.next_item
        count += 1
