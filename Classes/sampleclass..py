class PartyAnimal:
    x=0
    name=""

    #Constructor
    def __init__(self,z):
        self.name=z
        print("Iam constructed")

    def party(self):#METHOD
        self.x=self.x+1
        print(self.name,"Party count",self.x)

    #destructor
    def __del__(self):
        print("Iam destructed",self.x)

cb=PartyAnimal("Charlie-Black")#instance of class PartyAnimall
cb.party()
cb.party()
cb=42
print("an contains",cb)

print("Type",type(cb))
print(dir(cb))