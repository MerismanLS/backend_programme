from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    surname: str
    age: int
    love_dish_id: int

    @staticmethod
    def making_car_object(data: tuple):
        return User(data[0], data[1], data[2], data[3], data[4])

    def getting_data(self):
        return self.id, self.name, self.surname, self.age, self.love_dish_id
