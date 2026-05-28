#peyton mcadams
#the grocery store arrays

items = [
    "Milk", "Eggs", "Bread", "Butter", "Cheese",
    "Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Sausage",
    "Pasta", "Rice", "Quinoa", "Cereal", "Oatmeal",
    "Apples", "Bananas", "Oranges", "Strawberries", "Blueberries",
    "Grapes", "Pineapple", "Mangoes", "Lemons", "Limes",
    "Potatoes", "Onions", "Garlic", "Carrots", "Broccoli",
    "Cauliflower", "Spinach", "Kale", "Lettuce", "Bell Peppers",
    "Tomatoes", "Cucumbers", "Zucchini", "Mushrooms", "Avocados",
    "Olive Oil", "Vegetable Oil", "Cooking Spray", "Salt", "Pepper",
    "Sugar", "Brown Sugar", "Flour", "Baking Powder", "Baking Soda",
    "Peanut Butter", "Jelly", "Honey", "Maple Syrup", "Nutella",
    "Coffee", "Tea", "Hot Chocolate", "Creamer", "Sugar Packets",
    "Orange Juice", "Apple Juice", "Soda", "Sparkling Water", "Sports Drink",
    "Chips", "Crackers", "Pretzels", "Popcorn", "Cookies",
    "Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Frozen Chicken Nuggets", "Frozen Waffles",
    "Canned Soup", "Canned Beans", "Canned Corn", "Canned Tomatoes", "Canned Tuna",
    "Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Hot Sauce",
    "Paper Towels", "Toilet Paper", "Facial Tissues", "Dish Soap", "Laundry Detergent"
]

prices = [
    3.49, 2.99, 2.79, 3.99, 4.59,
    7.99, 6.49, 5.99, 4.99, 4.49,
    1.79, 4.29, 5.99, 3.99, 3.49,
    4.49, 1.39, 3.99, 4.99, 5.49,
    5.49, 3.49, 4.99, 1.79, 1.79,
    3.99, 2.49, 1.29, 2.29, 2.99,
    3.49, 3.49, 3.99, 2.49, 3.49,
    2.99, 1.79, 2.49, 2.99, 1.99,
    7.99, 5.49, 3.99, 1.29, 2.49,
    2.49, 2.99, 3.49, 2.49, 1.99,
    3.99, 3.29, 4.99, 6.99, 5.49,
    9.99, 4.49, 3.99, 2.49, 1.99,
    4.29, 3.99, 1.99, 2.49, 2.99,
    3.99, 3.49, 2.99, 2.49, 4.99,
    5.99, 6.49, 2.99, 7.49, 4.99,
    2.79, 1.49, 1.29, 1.79, 2.49,
    2.99, 2.49, 4.49, 3.49, 3.99,
    8.99, 12.99, 3.99, 2.99, 11.99
]

def price_check(item_name):
    for i in range(len(items)):
        if items[i] == item_name:
            print(items[i])
            return (prices[i])

def discount(amount):
    for i in range(len(prices)):
        prices [i] = round(prices[i]*(1-(amount)),2)
        print(prices[i])

def cheaper(number):
    new_list = []
    for i in range(len(items)):
        if prices[i] < number:
            new_list.append(items[i])
    print(new_list)

#main
discount(0.2)
print("Here's what you can buy with $2: ")
cheaper(2)
print(round(price_check("Frozen Waffles")+price_check("Coffee")+price_check("Sugar")+price_check("Maple Syrup")+price_check("Butter"),2))
