#Food delivery app

class FoodItem:
    def __init__(self, food_id, name, price):
        self.food_id = food_id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.food_id}. {self.name} - ₹{self.price}")


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []

    def add_food(self, food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\n----- {self.name} Menu -----")
        for item in self.menu:
            item.display()

    def get_food(self, food_id):
        for item in self.menu:
            if item.food_id == food_id:
                return item
        return None


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, food):
        self.cart.append(food)
        print(f"{food.name} added to cart.")

    def remove_from_cart(self, food_id):
        for item in self.cart:
            if item.food_id == food_id:
                self.cart.remove(item)
                print(f"{item.name} removed from cart.")
                return
        print("Food item not found in cart.")

    def view_cart(self):
        if len(self.cart) == 0:
            print("\nCart is Empty.")
            return

        print("\n------ Your Cart ------")
        total = 0

        for item in self.cart:
            print(f"{item.name} - ₹{item.price}")
            total += item.price

        print("------------------------")
        print("Total = ₹", total)

    def checkout(self):
        if len(self.cart) == 0:
            print("Cart is Empty.")
            return

        total = sum(item.price for item in self.cart)

        print("\n========= BILL =========")
        for item in self.cart:
            print(f"{item.name:20} ₹{item.price}")

        gst = total * 0.05
        final = total + gst

        print("-------------------------")
        print(f"Subtotal : ₹{total}")
        print(f"GST (5%) : ₹{gst:.2f}")
        print(f"Total    : ₹{final:.2f}")
        print("=========================")

        print("Order Placed Successfully!")
        self.cart.clear()


# ---------------- Main Program ----------------

restaurant = Restaurant("Food Hub")

restaurant.add_food(FoodItem(1, "Pizza", 250))
restaurant.add_food(FoodItem(2, "Burger", 120))
restaurant.add_food(FoodItem(3, "Pasta", 180))
restaurant.add_food(FoodItem(4, "Momos", 90))
restaurant.add_food(FoodItem(5, "Cold Drink", 60))

name = input("Enter Customer Name: ")
customer = Customer(name)

while True:

    print("\n========== FOOD DELIVERY APP ==========")
    print("1. Show Menu")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        restaurant.show_menu()

    elif choice == 2:
        restaurant.show_menu()
        food_id = int(input("Enter Food ID: "))

        food = restaurant.get_food(food_id)

        if food:
            customer.add_to_cart(food)
        else:
            print("Invalid Food ID.")

    elif choice == 3:
        food_id = int(input("Enter Food ID to Remove: "))
        customer.remove_from_cart(food_id)

    elif choice == 4:
        customer.view_cart()

    elif choice == 5:
        customer.checkout()

    elif choice == 6:
        print("Thank You for Using Food Delivery App!")
        break

    else:
        print("Invalid Choice.")