class Pizza:
    def __init__(self, name, ingredients, price):
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def display_pizza_information(self):
        print(f"Pizza: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Price: £{self.price}")

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        print(f"{ingredient} added to {self.name}")

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredient.remove(ingredient)
            print(f"{ingredient} removed from {self.name}")
        else:
            print(f"{ingredient} not in {self.name}")


margherita = Pizza("Margherita", ["Tomato sauce", "Mozzarella", "Basil"], 8.00)
hawaiian = Pizza("Hawaiian", ["Tomato sauce", "Mozzarella", "Pineapple"], 10.00)
veggie = Pizza("Veggie", ["Tomato sauce", "Mozzarella", "Bell peppers", "Onions", "Mushrooms", "Olives"], 9.00)
four_cheese = Pizza("Four Cheese", ["Tomato sauce", "Mozzarella", "Cheddar", "Parmesan", "Blue cheese"], 11.50)
mexican = Pizza("Mexican", ["Tomato sauce", "Mozzarella", "Jalapenos", "Onions", "Bell peppers"], 11.00)
garden_fresh = Pizza("Garden Fresh", ["Tomato sauce", "Mozzarella", "Spinach", "Artichokes", "Cherry tomatoes"], 9.50)



margherita.display_pizza_information()