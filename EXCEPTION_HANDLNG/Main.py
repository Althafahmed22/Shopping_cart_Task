class ShoppingCart:
    def __init__(self, item_quantity, price):
        self.item_quantity = item_quantity
        self.price = price
        self.cart_quantity = 0
    def add_to_cart(self):
        try:
            quantity_to_add = int(input(f"Enter quantity to add (Stock: {self.item_quantity}): "))
            try:
                if quantity_to_add <= 0 or quantity_to_add > self.item_quantity:
                    raise ValueError("Invalid quantity.")
                self.cart_quantity += quantity_to_add
                self.item_quantity -= quantity_to_add
            except ValueError as ve:
                print(f"Error in quantity: {ve}")
        except ValueError:
            print("Please enter a valid number for quantity.")
        finally:
            print("......................")
    def applying_discount(self):
        try:
            discount_code = input("Enter discount code: ")
            try:
                if discount_code not in ['SAVED', 'CHRIS112', 'CODE2025']:
                    raise ValueError("Invalid code.")
                print("Discount applied: 10% off.")
            except ValueError as ve:
                print(f"Error in discount: {ve}")
        except Exception:
            print("Unexpected error during discount validation.")
        finally:
            print("Discount validation finished.")
    def checkout(self):
        self.add_to_cart()
        self.applying_discount()
        print(f"Total: ${self.cart_quantity * self.price}")
        print("Checkout completed.")
cart = ShoppingCart(item_quantity=5, price=100)
cart.checkout()




