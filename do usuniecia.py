def shopping():
    shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    shopping_cart = "Koszyk zawiera: "
    for item in shopping_items:
        shopping_cart += item + '\n'
    return shopping_cart

shopping_result = shopping()
print(shopping_result)