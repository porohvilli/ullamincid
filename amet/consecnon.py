recipe = {
    "title": "Spaghetti Bolognese",
    "ingredients": ["spaghetti", "ground beef", "onion", "garlic", "tomato sauce", "olive oil", "salt", "pepper"]
}

for ingredient in recipe["ingredients"]:
    print("Ingredient:", ingredient)
    for letter in ingredient:
        print("Letter:", letter)
