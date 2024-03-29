from dataclasses import dataclass

@dataclass
class Dish:
    id: int
    name: str
    calories: int
    proteins: int
    fats: int
    carbos: int # carbohydrates - углеводы

    @staticmethod
    def making_dish_object(data: tuple):
        return Dish(data[0], data[1], data[2], data[3], data[4], data[5])

    def getting_data(self):
        return self.id, self.name, self.calories, \
            self.proteins, self.fats, self.carbos