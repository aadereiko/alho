from collections import Counter


class QueueItem:
    def __init__(self, item, priority = 0):
        self.item = item
        self.priority = priority

    def __repr__(self):
        return f'{self.item}: {self.priority}'


class Node:
    def __init__(self, symbol='', freq = 0, left=None, right=None, parent=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.parent = parent

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left or self.right)

    def set_parent(self, parent):
        self.parent = parent


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size


def position_to_add(queue, elem):
    if not len(queue):
        return 0

    for index in range(0, len(queue)):
        if queue[index].priority >= elem.priority:
            return index

    return len(queue)

prior_queue = []

symbols = Counter(input())
print(symbols)

for key in symbols:
    elem = QueueItem(key, symbols[key])
    index = position_to_add(prior_queue, elem)
    prior_queue[index:index] = [elem]


# check count
nodes = None
for _ in range(0, len(prior_queue) - 1):
    left = Node(symbol=prior_queue[0].item)
    right = Node(symbol=prior_queue[1].item)
    parent = Node(left=left, right=right)
    left.set_parent(parent)
    right.set_parent(parent)




print(prior_queue)