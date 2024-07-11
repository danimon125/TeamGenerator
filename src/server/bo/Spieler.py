from server.bo.BusinessObject import BusinessObject


class Spieler(BusinessObject):

    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Fridge()."""
        obj = Spieler()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])

        return obj