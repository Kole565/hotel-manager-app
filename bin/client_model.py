"""Provide model class for item serialization."""


class ClientModel:
    """Data class for item serialization."""

    TABLE_NAME = "clients"

    def __init__(self, password_hash, username, name, credentials):
        """Store init data in class."""
        self._password_hash = password_hash
        self._username = username
        self._name = name
        self._credentials = credentials

    @property
    def password_hash(self):
        """Getter for password hash property."""
        return self._password_hash

    @password_hash.setter
    def password_hash(self, value):
        """Setter for password hash property."""
        self._password_hash = value

    @property
    def username(self):
        """Getter for username property."""
        return self._username

    @username.setter
    def username(self, value):
        """Setter for username property."""
        self._username = value

    @property
    def name(self):
        """Getter for fio property."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for fio property."""
        self._name = value

    @property
    def credentials(self):
        """Getter for credentials property."""
        return self._credentials

    @credentials.setter
    def credentials(self, value):
        """Setter for credentials property."""
        self._credentials = value

    def save(self, db):
        """From query and put model data in db."""
        db.connect()

        db.execute(self._get_save_query(), self._get_save_arguments())
        db.commit()

        db.disconnect()

    def _get_save_query(self):
        query = "INSERT INTO {} (password_hash, username, fio, credentials) \
        VALUES (%s, %s, %s, %s)".format(self.TABLE_NAME)

        return query

    def _get_save_arguments(self):
        return (
            self._password_hash, self._username, self._name, self._credentials
        )

    @staticmethod
    def from_table(id, password_hash, username, name, credentials):
        """Create model from data acquired from respective table in db."""
        return ClientModel(
            password_hash=password_hash, username=username, name=name,
            credentials=credentials
        )
