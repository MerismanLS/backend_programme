from dataclasses import dataclass

@dataclass
class Dish:
    id: int | None
    name: str
    calories: int
    proteins: int
    fats: int
    carbos: int # carbohydrates - углеводы

    @staticmethod
    def of(data: tuple):
        return Dish(data[0], data[1], data[2], data[3], data[4], data[5])

    def to_data(self):
        return self.name, self.calories, \
            self.proteins, self.fats, self.carbos

    def get(self):
        return (str(self.id), self.name,
                str(self.calories), str(self.proteins),
                str(self.fats), str(self.carbos))
