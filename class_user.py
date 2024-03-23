class User:
    def __init__(self, id, name, surname, age, love_dish_id):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.love_dish_id = love_dish_id

# каждое свойство можно сделать приватным
# и прописать к нему getter и setter
