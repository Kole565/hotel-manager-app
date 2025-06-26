class ClientModel:

    TABLE_NAME = "clients"

    def __init__(self, password_hash, username, name, credentials):
        self._password_hash = password_hash
        self._username = username
        self._name = name
        self._credentials = credentials

    @property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        self._password_hash = value

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        self._credentials = value

    def save(self, db):
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (password_hash, username, fio, credentials) VALUES (%s, %s, %s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return self._password_hash, self._username, self._name, self._credentials

    @staticmethod
    def from_table(id, password_hash, username, name, credentials):
        return ClientModel(password_hash=password_hash, username=username, name=name, credentials=credentials)
