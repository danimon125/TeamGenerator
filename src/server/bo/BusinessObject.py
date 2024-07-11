from abc import ABC

class BusinessObject(ABC):
    
    def __init__(self):
        self._id = 0

    def get_id(self):
        return self._id
    
    def set_id(self, value):
        self._id = value
        