class Dish:
    def __init__(self, id, name, calories, proteins, fats, carbos):
        self.id = id
        self.name = name
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbos = carbos  # carbohydrates - углеводы

# каждое свойство можно сделать приватным
# и прописать к нему getter и setter
