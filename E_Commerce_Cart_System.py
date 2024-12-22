def cal_total_price(cart_items):
    if len(cart_items) == 0:
        return "Cart is Empty"
    
    total = sum(cart_items.values())

    if len(cart_items) > 5:
        total *= 0.9
        
    return total

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(f"Total Price: {cal_total_price(cart_items)}")
