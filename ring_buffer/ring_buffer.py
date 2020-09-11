class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.item_ring  = list()
        self.item_remove = 0

    def append(self, item):
        if len(self.item_ring) < self.capacity:
            self.item_ring.append(item)
        else:
            self.item_ring.pop(self.item_remove)
            self.item_ring.insert(self.item_remove, item)
            if self.item_remove == self.capacity -1:
                self.item_remove = 0
            else:
                self.item_remove += 1

    def get(self):
        return self.item_ring