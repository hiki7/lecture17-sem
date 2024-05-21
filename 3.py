class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def print_ingredients(self):
        print(f"Ингредиенты для {self.name}:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")

    def cook(self):
        print(f"""Сегодня мы готовим {self.name}.
Выполняем инструкцию по приготовлению блюда {self.name}...
Блюдо {self.name} готово!""")


spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
spaghetti.print_ingredients()
spaghetti.cook()
