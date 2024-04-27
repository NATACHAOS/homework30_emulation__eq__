class Building:
    def __init__(self, *args):
        self.numberOfFloors = int()
        self.buildingType = str()

    def __eq__(self, other):
        return self.numberOfFloors == self.buildingType


obj1 = Building()
obj2 = Building()

if Building.__eq__(self=obj1, other=obj2):
    print('Мы равны)')
else:
    print('Мы не равны')

print(obj1 == obj2)
