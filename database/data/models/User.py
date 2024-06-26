from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    surname: str
    age: int
    love_dish_id: int
    comments: str
    login: str
    password: str

    @staticmethod
    def of(data: tuple):
        return User(data[0], data[1], data[2], data[3], data[4], data[5])

    def to_data(self):
        return self.name, self.surname, \
            self.age, self.love_dish_id, self.comments, \
            self.login, self.password

    def get(self):
        return (str(self.id), self.name,
                str(self.surname), str(self.age),
                str(self.love_dish_id), str(self.comments))