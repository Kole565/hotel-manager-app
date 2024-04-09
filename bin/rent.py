class Rent:

    USER_NAME = "kole"
    DB_NAME = "hotel"
    TABLE_NAME = "rents"

    def __init__(self, duration, since, due=None, index=None):
        self._duration = duration
        self._since = since
        self._due = self._since + self._duration

        self._index = index

        self._rooms = []
        self._clients = []

    def add_room(self, index):
        self._rooms.append(index)

    def add_client(self, index):
        self._clients.append(index)
