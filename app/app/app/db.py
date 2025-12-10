class InMemoryDB:
    def __init__(self):
        self.storage = {}

    def save(self, key, value):
        self.storage[key] = value

    def get(self, key):
        return self.storage.get(key)

db = InMemoryDB()
