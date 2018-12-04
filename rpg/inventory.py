class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, items):
        self.slots.append(items)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        for item in self.slots:
            yield item
        # "yield from self.slots" can be used instead of the whole "for loop"

    