class Recipe:
    def __init__(self, recipe_name, ingredient, cooking_time, instructions):
        self.recipe_name = recipe_name
        self.ingredient = ingredient
        self.cooking_time = cooking_time
        self.instructions = instructions

    def display(self):
        print(f"Name: {self.recipe_name}")
        print(f"Ingredient: {self.ingredient}")
        print(f"Cooking time: {self.cooking_time}")
        print(f"Instructions: {self.instructions}")
        print("_" * 20)


def create_recipe():
    recipe_name = input("Enter recipe name: ")
    ingredient = input("Enter ingredients (comma-separated): ")
    cooking_time = input("Enter cooking time: ")
    instructions = input("Enter cooking instructions: ")
    return Recipe(recipe_name, ingredient, cooking_time, instructions)


print("Welcome to Recipe Collection\n")

my_recipe = create_recipe()

print("Recipe added successfully\n")
print("Displaying recipe...")

my_recipe.display()