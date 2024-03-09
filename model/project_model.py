from sys import maxsize

class Project:

    def __init__(self, id=None, name=None, status=None, inherit=None, enabled=None, view_status=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.inherit = inherit
        self.enabled = enabled
        self.view_status = view_status
        self.description = description


    def __repr__(self):
        return f'\n{self.id},{self.name},{self.status},{self.enabled},{self.view_status},{self.description}'

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize