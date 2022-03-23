class Pet:
    def __init__(self,name):
        self._name=name

    @classmethod
    def name(self):
     return self._name

pet=Pet('Max')
print(pet.__dict__)

