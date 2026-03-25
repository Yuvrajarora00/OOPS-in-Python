class Shopping:
    def __init__(self):
        self.store = {"milk": 59, "soap": 92, "rice": 94, "wheat": 53}
        self.cart = {}
        self.total = 0

    def show_store(self):
        print("Available items:")
        for item, price in self.store.items():
            print(f"{item} : {price}")

    def add_item(self, item):
        if item in self.store:
            self.cart[item] = self.store[item]
            self.total += self.store[item]
            print(f"{item} added to cart")
        else:
            print("Item not available")

    def remove_item(self, item):
        if item in self.cart:
            self.total -= self.cart[item]
            del self.cart[item]
            print(f"{item} removed")
        else:
            print("Item not in cart")

    def show_cart(self):
        print("Cart items:", self.cart)

    def total_price(self):
        print("Total is:", self.total)


# usage
s = Shopping()

s.show_store()

s.add_item("milk")
s.add_item("rice")

s.show_cart()
s.total_price()

s.remove_item("milk")

s.show_cart()
s.total_price()
