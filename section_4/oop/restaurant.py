class Restaurant:

    '''
    class Restaurant has id, name, cuisine, and list of dishes
    '''

    count = 1
    
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.dishes = []

        self.id = Restaurant.count
        Restaurant.count += 1

    def add_dish(self, new_dish):
        self.dishes.append(new_dish)
 
    def __str__(self):
        dishes_str = []
        for dish in self.dishes:
            dishes_str.append(dish.__str__())
        return "%s serves %s and has the following dishes: %s" % (self.name, self.cuisine, "\n".join(dishes_str))

class Dish:
    '''
    class Dish has name, list of ingredients, and a spicy level
    '''
    def __init__(self, name, ingredients, spicy_level):
        self.name = name
        self.ingredients = ingredients
        self.spicy_level = spicy_level

    def __str__(self):
        return "%s contains %s and has a spicy level of %d" % (self.name, ", ".join(self.ingredients), self.spicy_level)
    
    def change_spicy_level(self, new_level):
        self.spicy_level = new_level

def main():
    mcdonalds = Restaurant("McDonalds", "fast-food")
    mcdonalds.add_dish(Dish("Big Mac", ["beef", "cheese"], 0))
    # print(mcdonalds.__str__())
    mcdonalds.add_dish(Dish("Nuggets", ["Chicken", "bread"], 0))

    print(mcdonalds)

if __name__ == "__main__":
    main()

