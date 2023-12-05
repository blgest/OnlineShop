class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({'product': product, 'quantity': quantity})

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
