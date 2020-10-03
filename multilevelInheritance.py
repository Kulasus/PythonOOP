class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("Number of strings is {}, guitar is made of {} and it can play {} keys".format(self.numberOfStrings, self.typeOfWood, self.numberOfMajorKeys))

guitar = Guitar()