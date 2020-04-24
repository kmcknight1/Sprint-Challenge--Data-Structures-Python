from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if length of the list is less than capacity, add item to tail and make current the head
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            # if current has a next, set that spot to the new item, make the next node the new current
            if self.current.next:
                self.current.value = item
                self.current = self.current.next
            else:
                # if current is tail, set that spot to the new item, make the head the new current
                self.current.value = item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # start at head, loop through and append each node.value to the list (making node = next to move through)
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        # storage is an array with available slots based on capacity
        self.storage = [None] * capacity
        self.current_index = 0
        self.capacity = capacity

    def append(self, item):
        # set the item in place of the current
        self.storage[self.current_index] = item

        # move the current_index to the beginning of the list
        if self.current_index == self.capacity-1:
            self.current_index = 0
        # move the current_index up one, to be the new item
        else:
            self.current_index += 1

    def get(self):
        return [item for item in self.storage if item]
