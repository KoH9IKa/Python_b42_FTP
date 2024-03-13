from sys import maxsize


class User:

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'{self.username}'

    # def __eq__(self, other):
    #     return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name
    #
    # def id_or_max(self):
    #     if self.id:
    #         return int(self.id)
    #     else:
    #         return maxsize
