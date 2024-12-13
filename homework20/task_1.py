import json

# Market and Recipe Data
with open('homework20/homework_1_markets.json', 'r') as file:
    markets_data = json.load(file)

with open('homework20/homework_1_recipes.json', 'r') as file:
    recipes_data = json.load(file)

def find_minimum_markets(dish, recipes_data, markets_data):
    
    required_ingredients = set(recipes_data[dish]['ingredients'])
    markets_selected = []
    covered_ingredients = set()

    while required_ingredients:
        # Find the market that provides the most uncovered ingredients
        best_market = None
        ingredients_covered_by_market = set()

        for market, products in markets_data.items():
            uncovered_products = required_ingredients & set(products)
            if len(uncovered_products) > len(ingredients_covered_by_market):
                best_market = market
                ingredients_covered_by_market = uncovered_products

        if not best_market:  # No market can provide the remaining ingredients
            return f"Cannot find all ingredients for {dish} in this city. Missing: {required_ingredients}"

        # Add the best market to the selection
        markets_selected.append(best_market)
        covered_ingredients.update(ingredients_covered_by_market)
        required_ingredients -= ingredients_covered_by_market

    return markets_selected, covered_ingredients

def main():
    input_dish = 'Chicken Curry'
    result = find_minimum_markets(input_dish, recipes_data, markets_data)

    selected_markets, ingredients_covered = result #zip
    print(f"To make '{input_dish}', you need to visit the following markets: {', '.join(selected_markets)}")
    print(f"These markets provide all the required ingredients: {', '.join(ingredients_covered)}")
if __name__ == '__main__':
    main()
    