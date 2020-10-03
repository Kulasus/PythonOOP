class Furniture:
    material = "Teakwood"

class Chair(Furniture):
    __numberOfLegs = 4
    def changeMaterial(self, material):
        self.material = material
    
