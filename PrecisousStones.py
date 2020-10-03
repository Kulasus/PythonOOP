class StoneCollection:
    #Collection init
    def __init__(self,name):
        self.name = name
        self.collection = []
    #Adding items to collection
    def addToCollection(self, stone):
        if len(self.collection) == 5:
            for x in range(len(self.collection)-1):
                self.collection[x] = self.collection[x+1]
            self.collection[len(self.collection)-1] = stone
        else:
            self.collection.append(stone)
    #Printing collection info
    def info(self):
        for x in range(len(self.collection)):
            print(self.collection[x].info())

class Stone:
    #Stone obj init
    def __init__(self, name):
        self.name = name
    #Printing stone info
    def info(self):
        print(self.name)


s1 = Stone("Diamond")
s2 = Stone("Ruby")
s3 = Stone("Aquamarine")
s4 = Stone("Granate")
s5 = Stone("Emerald")
s6 = Stone("Enderit")

sc1 = StoneCollection("myStoneCollection")
sc1.addToCollection(s1)
sc1.addToCollection(s2)
sc1.addToCollection(s3)
sc1.addToCollection(s4)
sc1.addToCollection(s5)
sc1.addToCollection(s6)
sc1.addToCollection(s1)
sc1.info()