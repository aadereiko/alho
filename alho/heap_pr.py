class BinaryCompletedHeap:
    def __init__(self):
        self.elements = []

    def insert(self, positive_element):
        element = -positive_element
        current_index = len(self.elements)
        self.elements.append(element)
        if len(self.elements):
            parent_index = (current_index - 1) // 2

            while parent_index >= 0 and self.elements[parent_index] > self.elements[current_index]:
                self.elements[parent_index], self.elements[current_index] = self.elements[current_index], self.elements[parent_index]
                current_index = parent_index
                parent_index = (current_index - 1) // 2
        else:
            self.elements.append(element)

    def __len__(self):
        return len(self.elements)

    def _choose_child_index(self, parent_index):
        left_index, right_index = 2 * parent_index + 1, 2 * parent_index + 2
        if left_index >= len(self.elements):
            return parent_index, parent_index

        result = left_index if right_index >= len(self.elements) or \
                               min(self.elements[left_index], self.elements[right_index]) == self.elements[left_index] \
            else right_index
        return result, left_index

    def extract_max(self):
        max_element = 0
        if len(self.elements) == 1:
            max_element = -self.elements[0]
            self.elements = []

        if len(self.elements):
            max_element = -self.elements[0]

            self.elements[0] = self.elements.pop()
            parent_index = 0
            child_index, left_index = self._choose_child_index(parent_index)
            while left_index < len(self.elements) and self.elements[parent_index] > self.elements[child_index]:
                self.elements[parent_index], self.elements[child_index] = self.elements[child_index], self.elements[parent_index]
                parent_index = child_index
                child_index, left_index = self._choose_child_index(parent_index)

        return max_element

    def __repr__(self):
        return ', '.join(map(str, self.elements))


example = BinaryCompletedHeap()
amount = int(input())

for _ in range(0, amount):
    line = input().split(' ')
    if len(line) == 1:
        print(example.extract_max())
    elif len(line) == 2:
        example.insert(int(line[1]))