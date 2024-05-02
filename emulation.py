class Building:
    """Здание"""

    def __init__(self):
        self.numberOfFloors = 10  # атрибут этажности
        self.buildingType = 'Здание'  # название

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        # сравниваем одинаковые атрибуты этажности и названия

obj1 = Building()
obj2 = Building()
print(obj1 == obj2)

obj2.numberOfFloors = 10
obj2.buildingType = 'Сооружение' # "Здание" не "Сооружение". На консоли выводится False
print(obj1 == obj2)
